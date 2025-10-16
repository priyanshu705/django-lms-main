#!/usr/bin/env python3
"""
SavvyIndians LMS - Admin Credential Manager
This script allows you to change admin username and password easily
"""

import os
import sys
import django
from getpass import getpass

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
# django.setup()  # Disabled to prevent reentrant initialization

from accounts.models import User

def change_admin_credentials():
    print("🔧 SavvyIndians LMS - Admin Credential Manager")
    print("=" * 50)
    
    # Show current admin users
    admins = User.objects.filter(is_superuser=True)
    print("\n📋 Current Admin Users:")
    for admin in admins:
        print(f"   • Username: {admin.username}")
        print(f"   • Email: {admin.email}")
    
    if not admins.exists():
        print("❌ No admin users found!")
        create_new = input("\n🤔 Would you like to create a new admin user? (y/n): ")
        if create_new.lower() == 'y':
            create_admin_user()
        return
    
    print(f"\n🎯 Found {admins.count()} admin user(s)")
    
    # Get current admin (assume first one if multiple)
    current_admin = admins.first()
    print(f"\n📝 Current Admin: {current_admin.username}")
    
    # Ask for new credentials
    print("\n🔄 Enter New Admin Credentials:")
    new_username = input(f"New Username (current: {current_admin.username}): ").strip()
    if not new_username:
        new_username = current_admin.username
        print(f"   → Keeping current username: {new_username}")
    
    new_email = input(f"New Email (current: {current_admin.email}): ").strip()
    if not new_email:
        new_email = current_admin.email
        print(f"   → Keeping current email: {new_email}")
    
    print("\n🔐 Enter New Password:")
    new_password = getpass("New Password: ")
    confirm_password = getpass("Confirm Password: ")
    
    if new_password != confirm_password:
        print("❌ Passwords don't match!")
        return
    
    if len(new_password) < 8:
        print("❌ Password must be at least 8 characters long!")
        return
    
    # Update admin credentials
    try:
        current_admin.username = new_username
        current_admin.email = new_email
        current_admin.set_password(new_password)
        current_admin.save()
        
        print("\n✅ Admin credentials updated successfully!")
        print(f"   • New Username: {new_username}")
        print(f"   • New Email: {new_email}")
        print(f"   • Password: Updated")
        
        print(f"\n🔗 Admin Panel: http://127.0.0.1:8000/admin/")
        print(f"   Login with: {new_username} / [your new password]")
        
    except Exception as e:
        print(f"❌ Error updating admin credentials: {e}")

def create_admin_user():
    print("\n🆕 Creating New Admin User:")
    username = input("Admin Username: ").strip()
    email = input("Admin Email: ").strip()
    
    if not username or not email:
        print("❌ Username and email are required!")
        return
    
    password = getpass("Admin Password: ")
    confirm_password = getpass("Confirm Password: ")
    
    if password != confirm_password:
        print("❌ Passwords don't match!")
        return
    
    if len(password) < 8:
        print("❌ Password must be at least 8 characters long!")
        return
    
    try:
        admin_user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f"\n✅ Admin user created successfully!")
        print(f"   • Username: {username}")
        print(f"   • Email: {email}")
        
    except Exception as e:
        print(f"❌ Error creating admin user: {e}")

if __name__ == "__main__":
    change_admin_credentials()