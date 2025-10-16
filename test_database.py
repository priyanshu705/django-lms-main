#!/usr/bin/env python
"""
SavvyIndians LMS - Database Connection Test
Test your Neon PostgreSQL database connection
"""

import os
import sys
import django
from django.conf import settings

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

def test_database_connection():
    """Test the database connection and display info"""
    from django.db import connection
    from django.core.management.color import no_style
    
    print("🚀 SAVVYINDIANS LMS - DATABASE CONNECTION TEST")
    print("=" * 60)
    
    try:
        # Test database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT version();")
            version = cursor.fetchone()[0]
            
            print("✅ DATABASE CONNECTION: SUCCESS")
            print(f"📊 Database: {connection.settings_dict['NAME']}")
            print(f"🏠 Host: {connection.settings_dict['HOST']}")
            print(f"👤 User: {connection.settings_dict['USER']}")
            print(f"🔢 Port: {connection.settings_dict['PORT']}")
            print(f"🐘 PostgreSQL Version: {version}")
            print()
            
            # Test basic database operations
            cursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'public';")
            table_count = cursor.fetchone()[0]
            print(f"📋 Tables in database: {table_count}")
            
            if table_count == 0:
                print("⚠️  No tables found - You need to run migrations!")
                print("   Run: python manage.py migrate")
            else:
                print("✅ Database has tables - Ready to use!")
                
                # List some tables
                cursor.execute("""
                    SELECT table_name 
                    FROM information_schema.tables 
                    WHERE table_schema = 'public' 
                    ORDER BY table_name 
                    LIMIT 10;
                """)
                tables = cursor.fetchall()
                if tables:
                    print("\n📋 Sample tables:")
                    for table in tables:
                        print(f"   • {table[0]}")
            
            print("\n🎉 YOUR NEON POSTGRESQL DATABASE IS READY!")
            return True
            
    except Exception as e:
        print("❌ DATABASE CONNECTION: FAILED")
        print(f"🚨 Error: {str(e)}")
        print("\n🔧 TROUBLESHOOTING:")
        print("1. Check your DATABASE_URL environment variable")
        print("2. Verify Neon database is running")
        print("3. Check network connectivity")
        print("4. Ensure psycopg2-binary is installed")
        return False

def show_django_settings():
    """Show current Django database settings"""
    print("\n⚙️  CURRENT DJANGO DATABASE SETTINGS:")
    print("-" * 40)
    db_settings = settings.DATABASES['default']
    for key, value in db_settings.items():
        if key == 'PASSWORD':
            print(f"{key}: {'*' * len(str(value)) if value else 'Not set'}")
        else:
            print(f"{key}: {value}")

if __name__ == "__main__":
    show_django_settings()
    print()
    success = test_database_connection()
    
    if success:
        print("\n✅ NEXT STEPS:")
        print("1. Deploy to Vercel: vercel --prod")
        print("2. Set DATABASE_URL in Vercel environment variables")
        print("3. Test your live SavvyIndians LMS!")
    else:
        print("\n🔧 FIX NEEDED:")
        print("1. Check your Neon database connection string")
        print("2. Verify environment variables")
        print("3. Try running: pip install psycopg2-binary")