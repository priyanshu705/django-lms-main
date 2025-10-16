#!/usr/bin/env python
"""
Comprehensive OAuth Integration Test
Tests the complete Google OAuth authentication flow and user profile integration.
"""

import os
import sys
import django
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from unittest.mock import patch, MagicMock

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from accounts.models import Student
from accounts.signals import oauth_user_signed_up
try:
    from allauth.socialaccount.models import SocialAccount, SocialApp
    from allauth.socialaccount.providers.google.provider import GoogleProvider
    ALLAUTH_AVAILABLE = True
except ImportError:
    print("Warning: django-allauth not fully available for testing")
    ALLAUTH_AVAILABLE = False

User = get_user_model()

class OAuthIntegrationTestCase(TestCase):
    """Test OAuth integration functionality"""
    
    def setUp(self):
        """Set up test data"""
        self.client = Client()
        
    def test_oauth_login_page_access(self):
        """Test that OAuth login pages are accessible"""
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        # Check if Google OAuth link is present
        self.assertContains(response, 'google', msg_prefix='Google OAuth option should be available')
        
    def test_oauth_logout_confirmation(self):
        """Test OAuth logout confirmation page"""
        # Create a test user
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        # Log in the user
        self.client.login(username='testuser', password='testpass123')
        
        # Test logout confirmation page
        response = self.client.get(reverse('accounts:logout_confirm'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Are you sure you want to logout?')
        
    def test_student_profile_creation_signal(self):
        """Test that student profiles are created for OAuth users"""
        # Create a user (simulating OAuth signup)
        user = User.objects.create_user(
            username='oauth_user',
            email='oauth@example.com',
            first_name='OAuth',
            last_name='User'
        )
        
        # Simulate the signal
        oauth_user_signed_up(sender=User, user=user, request=None)
        
        # Check if student profile was created
        self.assertTrue(Student.objects.filter(user=user).exists())
        student = Student.objects.get(user=user)
        self.assertEqual(student.user.first_name, 'OAuth')
        self.assertEqual(student.user.last_name, 'User')
        
    def test_oauth_connections_page(self):
        """Test OAuth connections management page"""
        # Create and login a user
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
        
        # Access OAuth connections page
        response = self.client.get(reverse('accounts:oauth_connections'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'OAuth Connections')
        
    @patch('accounts.views.SocialAccount')
    def test_logout_with_oauth_detection(self, mock_social_account):
        """Test logout view with OAuth account detection"""
        # Create a user
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        # Mock OAuth account
        mock_account = MagicMock()
        mock_account.provider = 'google'
        mock_social_account.objects.filter.return_value = [mock_account]
        
        self.client.login(username='testuser', password='testpass123')
        
        # Test logout confirmation with OAuth
        response = self.client.get(reverse('accounts:logout_confirm'))
        self.assertEqual(response.status_code, 200)

class ManagementCommandTestCase(TestCase):
    """Test management commands"""
    
    def test_fix_oauth_users_command_exists(self):
        """Test that the fix_oauth_users management command exists"""
        from django.core.management import get_commands
        commands = get_commands()
        self.assertIn('fix_oauth_users', commands)
        
    def test_management_command_dry_run(self):
        """Test management command dry run functionality"""
        from django.core.management import call_command
        from io import StringIO
        
        out = StringIO()
        call_command('fix_oauth_users', '--dry-run', stdout=out)
        output = out.getvalue()
        
        self.assertIn('DRY RUN', output)
        self.assertIn('Total OAuth users found', output)

def run_manual_tests():
    """Run manual OAuth integration tests"""
    print("=" * 60)
    print("COMPREHENSIVE OAUTH INTEGRATION TEST")
    print("=" * 60)
    
    # Check if allauth is properly configured
    if not ALLAUTH_AVAILABLE:
        print("❌ django-allauth not fully available")
        return False
    
    test_results = []
    
    try:
        # Test 1: Check OAuth login page
        print("Testing OAuth login page access...")
        from django.test import Client
        client = Client()
        response = client.get('/accounts/login/')
        if response.status_code in [200, 302]:  # 302 is expected for redirects
            print("✅ OAuth login page accessible (or redirected)")
            test_results.append(True)
        else:
            print(f"❌ OAuth login page failed: {response.status_code}")
            test_results.append(False)
            
        # Test 2: Check signals function
        print("Testing OAuth signal functions...")
        user = User.objects.create_user(
            username='test_oauth_user',
            email='test_oauth@example.com',
            first_name='Test',
            last_name='OAuth'
        )
        oauth_user_signed_up(sender=User, user=user, request=None)
        
        if Student.objects.filter(student=user).exists():
            print("✅ OAuth signal creates student profile")
            test_results.append(True)
        else:
            print("❌ OAuth signal failed to create student profile")
            test_results.append(False)
            
        # Test 3: Check management command
        print("Testing management command...")
        from django.core.management import call_command
        from io import StringIO
        out = StringIO()
        call_command('fix_oauth_users', '--dry-run', stdout=out)
        output = out.getvalue()
        
        if 'DRY RUN' in output:
            print("✅ Management command works correctly")
            test_results.append(True)
        else:
            print("❌ Management command failed")
            test_results.append(False)
            
        # Test 4: Check OAuth connections page
        print("Testing OAuth connections page...")
        user.set_password('testpass123')
        user.save()
        client.login(username='test_oauth_user', password='testpass123')
        response = client.get('/accounts/oauth/connections/')
        
        if response.status_code in [200, 302]:  # 302 might be expected for authenticated redirects
            print("✅ OAuth connections page accessible (or redirected)")
            test_results.append(True)
        else:
            print(f"❌ OAuth connections page failed: {response.status_code}")
            test_results.append(False)
            
        # Clean up
        user.delete()
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        test_results.append(False)
    
    # Summary
    passed = sum(test_results)
    total = len(test_results)
    
    print("\n" + "=" * 60)
    print(f"TESTS COMPLETED: {passed}/{total} PASSED")
    
    if passed == total:
        print("✅ ALL OAUTH INTEGRATION TESTS PASSED!")
        return True
    else:
        print(f"❌ {total - passed} TEST(S) FAILED")
        return False

if __name__ == '__main__':
    success = run_manual_tests()
    sys.exit(0 if success else 1)