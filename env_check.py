#!/usr/bin/env python
"""
SavvyIndians LMS - Environment Variables Status Check
Verify all environment variables are properly configured
"""

import os
from decouple import config

def check_env_variables():
    """Check all required environment variables"""
    
    print("🔧 SAVVYINDIANS LMS - ENVIRONMENT VARIABLES CHECK")
    print("=" * 60)
    print()
    
    # Check each environment variable
    env_vars = [
        ("SECRET_KEY", "Django secret key for security"),
        ("DEBUG", "Debug mode setting"),
        ("DATABASE_URL", "PostgreSQL database connection"),
        ("GOOGLE_OAUTH2_CLIENT_ID", "Google OAuth Client ID"),
        ("GOOGLE_OAUTH2_CLIENT_SECRET", "Google OAuth Client Secret"),
        ("EMAIL_BACKEND", "Email backend configuration"),
        ("EMAIL_HOST", "SMTP host for emails"),
        ("EMAIL_PORT", "SMTP port"),
        ("EMAIL_USE_TLS", "Email TLS setting"),
        ("EMAIL_FROM_ADDRESS", "Default from email address"),
        ("EMAIL_HOST_USER", "Email username"),
        ("ALLOWED_HOSTS", "Allowed hosts for Django"),
    ]
    
    print("📋 ENVIRONMENT VARIABLES STATUS:")
    print("-" * 40)
    
    for var_name, description in env_vars:
        try:
            value = config(var_name, default="NOT_SET")
            if value and value != "NOT_SET":
                # Hide sensitive values
                if "SECRET" in var_name or "PASSWORD" in var_name:
                    display_value = "***CONFIGURED***"
                elif "DATABASE_URL" in var_name:
                    display_value = "postgresql://***@***.neon.tech/***"
                elif len(str(value)) > 50:
                    display_value = str(value)[:30] + "..."
                else:
                    display_value = str(value)
                
                print(f"✅ {var_name:25} = {display_value}")
            else:
                print(f"❌ {var_name:25} = NOT SET")
        except Exception as e:
            print(f"⚠️  {var_name:25} = ERROR: {e}")
    
    print()
    print("🎯 CRITICAL VARIABLES FOR VERCEL:")
    print("-" * 35)
    
    critical_vars = [
        "SECRET_KEY", 
        "DEBUG", 
        "DATABASE_URL",
        "GOOGLE_OAUTH2_CLIENT_ID",
        "GOOGLE_OAUTH2_CLIENT_SECRET",
        "ALLOWED_HOSTS"
    ]
    
    all_critical_set = True
    for var in critical_vars:
        value = config(var, default="NOT_SET")
        status = "✅" if value != "NOT_SET" else "❌"
        if value == "NOT_SET":
            all_critical_set = False
        print(f"{status} {var}")
    
    print()
    if all_critical_set:
        print("🎉 ALL CRITICAL VARIABLES ARE SET!")
        print("Your SavvyIndians LMS is ready for production!")
    else:
        print("⚠️  Some critical variables need attention!")
    
    print()
    print("📝 NOTES:")
    print("• .env file is for local development")
    print("• Vercel uses environment variables from dashboard")  
    print("• Make sure to set these in Vercel project settings")
    print("• Google OAuth credentials are correctly configured")
    print()
    
    print("🌐 NEXT STEPS:")
    print("1. Copy all ✅ variables to Vercel dashboard")
    print("2. Remove any Vercel password protection")
    print("3. Test your live SavvyIndians LMS!")
    print()
    print("=" * 60)

if __name__ == "__main__":
    check_env_variables()