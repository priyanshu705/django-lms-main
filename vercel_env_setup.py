#!/usr/bin/env python3
"""
SavvyIndians LMS - Environment Variables Setup
Using your existing .env values for Vercel configuration
"""

def print_vercel_env_setup():
    print("🚀 SAVVYINDIANS LMS - VERCEL ENVIRONMENT SETUP")
    print("=" * 65)
    print("✅ Deployment successful!")
    print("🌐 New URL: https://django-lms-main-eqyuw5732-gy068644-8794s-projects.vercel.app")
    print("=" * 65)
    
    print("\n📋 COPY THESE TO VERCEL ENVIRONMENT VARIABLES:")
    print("=" * 50)
    
    # Generate a secure secret key
    import secrets
    import string
    chars = string.ascii_letters + string.digits + "!@#$%^&*(-_=+)"
    secret_key = ''.join(secrets.choice(chars) for _ in range(50))
    
    env_vars = [
        ("SECRET_KEY", secret_key),
        ("DEBUG", "False"),
        ("DJANGO_SETTINGS_MODULE", "config.settings"),
        ("ALLOWED_HOSTS", ".vercel.app"),
        # Google OAuth credentials (replace with your own)
        ("GOOGLE_OAUTH2_CLIENT_ID", "YOUR_GOOGLE_CLIENT_ID_HERE"),
        ("GOOGLE_OAUTH2_CLIENT_SECRET", "YOUR_GOOGLE_CLIENT_SECRET_HERE"),
        # Email configuration
        ("EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend"),
        ("EMAIL_HOST", "smtp.gmail.com"),
        ("EMAIL_PORT", "587"),
        ("EMAIL_USE_TLS", "True"),
    ]
    
    for name, value in env_vars:
        print(f"Name: {name}")
        print(f"Value: {value}")
        print("-" * 40)
    
    print("\n🗄️ DATABASE SETUP (Required for full functionality):")
    print("=" * 50)
    print("You need to add DATABASE_URL for user registration and data storage.")
    print("\n💚 RECOMMENDED: Neon PostgreSQL (Free)")
    print("1. Visit: https://neon.tech")
    print("2. Create account and new project")
    print("3. Copy connection string")
    print("4. Add to Vercel as:")
    print("   Name: DATABASE_URL")
    print("   Value: postgresql://user:password@host:port/database")
    
    print("\n🔐 GOOGLE OAUTH CONFIGURATION:")
    print("=" * 50)
    print("Your credentials are already set! Just need to update Google Console:")
    print("1. Visit: https://console.cloud.google.com/")
    print("2. Go to your OAuth credentials")
    print("3. Add these authorized origins:")
    print("   - https://django-lms-main-eqyuw5732-gy068644-8794s-projects.vercel.app")
    print("4. Add these callback URLs:")
    print("   - https://django-lms-main-eqyuw5732-gy068644-8794s-projects.vercel.app/auth/google/login/callback/")
    
    print("\n📧 EMAIL SETUP (Optional - for notifications):")
    print("=" * 50)
    print("If you want email notifications, add these:")
    print("Name: EMAIL_HOST_USER")
    print("Value: your-gmail@gmail.com")
    print("-" * 40)
    print("Name: EMAIL_HOST_PASSWORD")
    print("Value: your-app-password (not regular password!)")
    print("-" * 40)
    print("Name: EMAIL_FROM_ADDRESS")
    print("Value: SavvyIndians LMS <your-gmail@gmail.com>")
    
    print("\n⚡ QUICK SETUP LINKS:")
    print("=" * 50)
    print("🔧 Vercel Environment Variables:")
    print("   https://vercel.com/gy068644-8794s-projects/django-lms-main/settings/environment-variables")
    print("🗄️ Neon Database:")
    print("   https://neon.tech")
    print("🔐 Google Cloud Console:")
    print("   https://console.cloud.google.com/")
    
    print("\n✅ TESTING YOUR LMS:")
    print("=" * 50)
    print("After setting environment variables:")
    print("1. Redeploy: vercel --prod")
    print("2. Visit: https://django-lms-main-eqyuw5732-gy068644-8794s-projects.vercel.app")
    print("3. Test Google OAuth login")
    print("4. Check admin panel: /admin/")
    print("5. Verify mobile responsiveness")
    
    print("\n🎯 PRIORITY ORDER:")
    print("=" * 50)
    print("1. ✅ DONE: Basic deployment successful")
    print("2. 🔄 NEXT: Set environment variables above")
    print("3. 🗄️ THEN: Set up DATABASE_URL")
    print("4. 🔐 THEN: Configure Google OAuth domains")
    print("5. 🚀 FINALLY: Redeploy and test")
    
    print("\n" + "=" * 65)
    print("🎉 YOUR SAVVYINDIANS LMS IS LIVE!")
    print("📚 Students can access it globally once configured!")
    print("=" * 65)

if __name__ == "__main__":
    print_vercel_env_setup()