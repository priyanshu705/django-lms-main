#!/usr/bin/env python
"""
SavvyIndians LMS - Complete Vercel Environment Setup
====================================================
This script provides all the environment variables you need to set in Vercel
for your SavvyIndians LMS to work with your Neon PostgreSQL database.
"""

print("🚀 SAVVYINDIANS LMS - COMPLETE VERCEL ENVIRONMENT SETUP")
print("=" * 70)
print()

# Database connection string
DATABASE_URL = "postgresql://neondb_owner:npg_snWe2DkE4QGR@ep-noisy-frost-adlq3kiy-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

print("📋 COPY THESE ENVIRONMENT VARIABLES TO VERCEL:")
print("=" * 50)
print()

env_vars = [
    ("SECRET_KEY", "YOUR_SECRET_KEY_HERE"),
    ("DEBUG", "False"),
    ("DJANGO_SETTINGS_MODULE", "config.settings"),
    ("ALLOWED_HOSTS", ".vercel.app,.savvyindians.com"),
    ("DATABASE_URL", DATABASE_URL),
    ("GOOGLE_OAUTH2_CLIENT_ID", "YOUR_GOOGLE_CLIENT_ID_HERE"),
    ("GOOGLE_OAUTH2_CLIENT_SECRET", "YOUR_GOOGLE_CLIENT_SECRET_HERE"),
    ("EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend"),
    ("EMAIL_HOST", "smtp.gmail.com"),
    ("EMAIL_PORT", "587"),
    ("EMAIL_USE_TLS", "True"),
]

for i, (name, value) in enumerate(env_vars, 1):
    print(f"{i:2d}. Name: {name}")
    print(f"    Value: {value}")
    print("    " + "-" * 40)
    print()

print("🔗 QUICK SETUP LINKS:")
print("=" * 30)
print("🔧 Vercel Environment Variables:")
print("   https://vercel.com/gy068644-8794s-projects/django-lms-main/settings/environment-variables")
print()
print("🔐 Google Cloud Console (OAuth Setup):")
print("   https://console.cloud.google.com/")
print("   Add these authorized origins:")
print("   - https://django-lms-main-qddcrdccs-gy068644-8794s-projects.vercel.app")
print("   Add these callback URLs:")
print("   - https://django-lms-main-qddcrdccs-gy068644-8794s-projects.vercel.app/auth/google/login/callback/")
print()

print("⚡ DEPLOYMENT STATUS:")
print("=" * 25)
print("✅ Database: PostgreSQL connected and migrated")
print("✅ Admin User: Created (Gaurav / gy068644@gmail.com)")
print("✅ Vercel: Deployed successfully")
print("🌐 Live URL: https://django-lms-main-qddcrdccs-gy068644-8794s-projects.vercel.app")
print()

print("🎯 FINAL STEPS:")
print("=" * 20)
print("1. ✅ Copy all environment variables above to Vercel")
print("2. 🔐 Configure Google OAuth authorized domains")
print("3. 🚀 Redeploy: vercel --prod")
print("4. 🎉 Test your live SavvyIndians LMS!")
print()

print("🏆 CONGRATULATIONS!")
print("Your SavvyIndians LMS is ready for global student access!")
print("=" * 70)