#!/usr/bin/env python
"""
SavvyIndians LMS - Deployment Status Check
Test the live deployment and report status
"""

import requests
import time

def test_deployment():
    """Test the live deployment"""
    
    print("🚀 SAVVYINDIANS LMS - DEPLOYMENT STATUS CHECK")
    print("=" * 55)
    print()
    
    # Latest deployment URL
    url = "https://django-lms-main-pfcfrw6c2-gy068644-8794s-projects.vercel.app"
    
    print(f"🌐 Testing: {url}")
    print("⏳ Checking status...")
    print()
    
    try:
        # Test the homepage
        response = requests.get(url, timeout=30)
        
        if response.status_code == 200:
            print("✅ SUCCESS! SavvyIndians LMS is LIVE!")
            print(f"✅ Status Code: {response.status_code}")
            print(f"✅ Response Time: {response.elapsed.total_seconds():.2f}s")
            print()
            
            # Check if it contains SavvyIndians branding
            if "savvyindians" in response.text.lower() or "savvy" in response.text.lower():
                print("✅ SavvyIndians branding detected!")
            else:
                print("⚠️  Standard Django response - branding may need verification")
            
            print()
            print("🎉 YOUR LMS IS WORKING!")
            print("📚 Students can now access the platform!")
            
        elif response.status_code == 500:
            print("❌ FUNCTION_INVOCATION_FAILED (500 Error)")
            print("🔧 The function is still crashing. Need to debug further.")
            print()
            print("📋 Common causes:")
            print("• Missing environment variables")
            print("• Import errors in Django apps")
            print("• Database connection issues")
            
        elif response.status_code == 404:
            print("❌ NOT_FOUND (404 Error)")
            print("🔧 Routing issue - function not found")
            
        else:
            print(f"⚠️  Unexpected status: {response.status_code}")
            print(f"Response: {response.text[:200]}...")
            
    except requests.exceptions.Timeout:
        print("⏳ TIMEOUT - Function taking too long (>30s)")
        print("🔧 May indicate cold start or configuration issues")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ CONNECTION ERROR: {e}")
        print("🔧 Network or DNS issues")
    
    print()
    print("=" * 55)

if __name__ == "__main__":
    test_deployment()