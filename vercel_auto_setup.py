#!/usr/bin/env python
"""
SavvyIndians LMS - Vercel Environment Variable Auto-Setup
This script will automatically set all required environment variables in Vercel
"""

import subprocess
import sys
import os

def run_command(command):
    """Run a command and return the result"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def set_vercel_env_var(name, value):
    """Set a single environment variable in Vercel"""
    print(f"Setting {name}...")
    
    # Escape special characters in the value
    escaped_value = value.replace('"', '\\"').replace('&', '\\&')
    
    command = f'vercel env add {name} production "{escaped_value}"'
    success, stdout, stderr = run_command(command)
    
    if success:
        print(f"✅ {name} set successfully")
        return True
    else:
        print(f"❌ Failed to set {name}: {stderr}")
        return False

def main():
    print("🚀 SAVVYINDIANS LMS - VERCEL AUTO-SETUP")
    print("=" * 50)
    print()
    
    # Environment variables to set (load from .env file or prompt user)
    env_vars = {
        "SECRET_KEY": "YOUR_SECRET_KEY_HERE",
        "DEBUG": "False",
        "DJANGO_SETTINGS_MODULE": "config.settings",
        "ALLOWED_HOSTS": ".vercel.app,.savvyindians.com",
        "DATABASE_URL": "YOUR_DATABASE_URL_HERE",
        "GOOGLE_OAUTH2_CLIENT_ID": "YOUR_GOOGLE_CLIENT_ID_HERE",
        "GOOGLE_OAUTH2_CLIENT_SECRET": "YOUR_GOOGLE_CLIENT_SECRET_HERE",
        "EMAIL_BACKEND": "django.core.mail.backends.smtp.EmailBackend",
        "EMAIL_HOST": "smtp.gmail.com",
        "EMAIL_PORT": "587",
        "EMAIL_USE_TLS": "True",
    }
    
    print("📋 Setting environment variables in Vercel...")
    print()
    
    success_count = 0
    total_count = len(env_vars)
    
    for name, value in env_vars.items():
        if set_vercel_env_var(name, value):
            success_count += 1
        print()
    
    print("=" * 50)
    print(f"✅ Successfully set: {success_count}/{total_count} variables")
    
    if success_count == total_count:
        print("🎉 All environment variables set successfully!")
        print()
        print("🚀 Now redeploying...")
        
        # Redeploy
        success, stdout, stderr = run_command("vercel --prod")
        if success:
            print("✅ Deployment successful!")
            print("🌐 Your SavvyIndians LMS should now be working!")
        else:
            print(f"❌ Deployment failed: {stderr}")
    else:
        print("⚠️  Some variables failed to set. Please set them manually:")
        print("   https://vercel.com/gy068644-8794s-projects/django-lms-main/settings/environment-variables")

if __name__ == "__main__":
    main()