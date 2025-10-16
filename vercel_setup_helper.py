#!/usr/bin/env python3
"""
SavvyIndians LMS - Vercel Setup Helper
Comprehensive guide for setting up environment variables and database
"""

import secrets
import string

def generate_secret_key():
    """Generate a secure Django secret key"""
    chars = string.ascii_letters + string.digits + "!@#$%^&*(-_=+)"
    return ''.join(secrets.choice(chars) for _ in range(50))

def print_setup_guide():
    print("🚀 SAVVYINDIANS LMS - VERCEL SETUP HELPER")
    print("=" * 60)
    print("Your LMS is deployed! Now let's configure it properly.")
    print("=" * 60)
    
    # Generate a new secret key
    secret_key = generate_secret_key()
    
    print("\n📋 STEP 1: ENVIRONMENT VARIABLES")
    print("Copy these to your Vercel Environment Variables page:")
    print("-" * 50)
    
    env_vars = [
        ("SECRET_KEY", secret_key),
        ("DEBUG", "False"),
        ("ALLOWED_HOSTS", ".vercel.app,.savvyindians.com"),
        ("DJANGO_SETTINGS_MODULE", "config.settings"),
    ]
    
    for name, value in env_vars:
        print(f"Name: {name}")
        print(f"Value: {value}")
        print("-" * 30)
    
    print("\n🗄️ STEP 2: DATABASE SETUP (Choose One Option)")
    print("=" * 50)
    
    print("\n💚 OPTION A: Neon PostgreSQL (Recommended - Free)")
    print("1. Visit: https://neon.tech")
    print("2. Create free account")
    print("3. Create new project")
    print("4. Copy connection string")
    print("5. Add to Vercel as DATABASE_URL")
    print("   Format: postgresql://user:password@host:port/database")
    
    print("\n🔷 OPTION B: Vercel Postgres")
    print("1. Go to Vercel Dashboard > Storage")
    print("2. Create new Postgres database")
    print("3. Connect to your project")
    print("4. Connection string will be auto-added")
    
    print("\n💜 OPTION C: Supabase (Alternative)")
    print("1. Visit: https://supabase.com")
    print("2. Create new project")
    print("3. Go to Settings > Database")
    print("4. Copy connection string")
    
    print("\n🔐 STEP 3: GOOGLE OAUTH SETUP")
    print("=" * 50)
    print("1. Visit: https://console.cloud.google.com/")
    print("2. Create/select project")
    print("3. Enable Google+ API")
    print("4. Create OAuth 2.0 credentials")
    print("5. Add authorized origins:")
    print("   - https://django-lms-main-g6i3mxty1-gy068644-8794s-projects.vercel.app")
    print("   - Your custom domain (if any)")
    print("6. Add callback URLs:")
    print("   - https://your-domain/auth/google/login/callback/")
    print("7. Copy Client ID and Secret to Vercel:")
    
    print("\nName: GOOGLE_OAUTH2_CLIENT_ID")
    print("Value: [Your Google Client ID]")
    print("-" * 30)
    print("Name: GOOGLE_OAUTH2_CLIENT_SECRET") 
    print("Value: [Your Google Client Secret]")
    print("-" * 30)
    
    print("\n📧 STEP 4: EMAIL CONFIGURATION (Optional)")
    print("=" * 50)
    print("For Gmail SMTP:")
    print("Name: EMAIL_BACKEND")
    print("Value: django.core.mail.backends.smtp.EmailBackend")
    print("-" * 30)
    print("Name: EMAIL_HOST")
    print("Value: smtp.gmail.com")
    print("-" * 30)
    print("Name: EMAIL_PORT")
    print("Value: 587")
    print("-" * 30)
    print("Name: EMAIL_USE_TLS")
    print("Value: True")
    print("-" * 30)
    print("Name: EMAIL_HOST_USER")
    print("Value: your-email@gmail.com")
    print("-" * 30)
    print("Name: EMAIL_HOST_PASSWORD")
    print("Value: your-app-password")
    print("-" * 30)
    
    print("\n💳 STEP 5: STRIPE PAYMENT SETUP (Optional)")
    print("=" * 50)
    print("1. Visit: https://stripe.com")
    print("2. Create account/login")
    print("3. Get API keys from Dashboard")
    print("4. Add to Vercel:")
    print("Name: STRIPE_PUBLISHABLE_KEY")
    print("Value: pk_test_...")
    print("-" * 30)
    print("Name: STRIPE_SECRET_KEY")
    print("Value: sk_test_...")
    print("-" * 30)
    
    print("\n🔒 STEP 6: SECURITY SETTINGS")
    print("=" * 50)
    print("Name: SECURE_SSL_REDIRECT")
    print("Value: True")
    print("-" * 30)
    
    print("\n✅ STEP 7: REDEPLOY")
    print("=" * 50)
    print("After setting all environment variables:")
    print("1. Go to Vercel Dashboard")
    print("2. Go to Deployments tab")
    print("3. Click 'Redeploy' on latest deployment")
    print("4. Or run: vercel --prod")
    
    print("\n🎯 STEP 8: TEST YOUR LMS")
    print("=" * 50)
    print("After redeployment, test these features:")
    print("✅ Homepage loads correctly")
    print("✅ Google OAuth login works")
    print("✅ Admin panel accessible")
    print("✅ Course content displays")
    print("✅ Mobile responsiveness")
    
    print("\n🔗 QUICK LINKS")
    print("=" * 50)
    print("🌐 Your LMS: https://django-lms-main-g6i3mxty1-gy068644-8794s-projects.vercel.app")
    print("⚙️ Vercel Dashboard: https://vercel.com/dashboard")
    print("🔧 Environment Variables: https://vercel.com/gy068644-8794s-projects/django-lms-main/settings/environment-variables")
    print("📊 Deployments: https://vercel.com/gy068644-8794s-projects/django-lms-main/deployments")
    
    print("\n🎉 COMPLETION CHECKLIST")
    print("=" * 50)
    checklist = [
        "□ Set SECRET_KEY environment variable",
        "□ Set DEBUG=False",
        "□ Configure DATABASE_URL with PostgreSQL",
        "□ Set up Google OAuth credentials",
        "□ Configure email settings (optional)",
        "□ Set up Stripe payments (optional)",
        "□ Redeploy application",
        "□ Test all functionality",
        "□ Verify mobile responsiveness",
        "□ Check admin panel access"
    ]
    
    for item in checklist:
        print(f"  {item}")
    
    print("\n" + "=" * 60)
    print("🚀董 YOUR SAVVYINDIANS LMS IS READY FOR STUDENTS!")
    print("📚 Happy Teaching! 🎓")
    print("=" * 60)

if __name__ == "__main__":
    print_setup_guide()
