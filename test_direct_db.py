#!/usr/bin/env python
"""
🔍 SAVVYINDIANS LMS - STANDALONE DATABASE TEST
=============================================
Direct PostgreSQL connection test bypassing Django
"""

import os
import json

def test_postgresql_direct():
    """Direct PostgreSQL connection test"""
    
    print("🔍 SAVVYINDIANS LMS - STANDALONE DATABASE TEST")
    print("=" * 60)
    print()
    
    # Get database URL from environment
    database_url = "postgresql://neondb_owner:npg_snWe2DkE4QGR@ep-noisy-frost-adlq3kiy-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
    
    print("🌐 Testing Direct PostgreSQL Connection...")
    print("🔗 Database: Neon PostgreSQL")
    print()
    
    try:
        # Try to import psycopg2
        try:
            import psycopg2
            print("✅ psycopg2: Available")
        except ImportError:
            print("❌ psycopg2: Not available")
            print("📦 Installing psycopg2-binary...")
            import subprocess
            subprocess.check_call(["pip", "install", "psycopg2-binary"])
            import psycopg2
            print("✅ psycopg2-binary: Installed successfully")
        
        # Parse database URL
        import urllib.parse
        url = urllib.parse.urlparse(database_url)
        
        print(f"🏠 Host: {url.hostname}")
        print(f"📊 Database: {url.path[1:]}")
        print(f"👤 User: {url.username}")
        print(f"🔢 Port: {url.port}")
        print()
        
        print("⏳ Connecting to database...")
        
        # Direct connection to PostgreSQL
        conn = psycopg2.connect(database_url)
        cursor = conn.cursor()
        
        print("✅ DATABASE CONNECTION: SUCCESS!")
        print()
        
        # Test basic queries
        print("🔍 Running Database Tests...")
        print("-" * 30)
        
        # Test 1: PostgreSQL version
        cursor.execute("SELECT version();")
        version = cursor.fetchone()[0]
        print(f"🐘 PostgreSQL Version: {version.split()[0]} {version.split()[1]}")
        
        # Test 2: Database name
        cursor.execute("SELECT current_database();")
        db_name = cursor.fetchone()[0]
        print(f"🗄️  Current Database: {db_name}")
        
        # Test 3: Current user
        cursor.execute("SELECT current_user;")
        db_user = cursor.fetchone()[0]
        print(f"👤 Current User: {db_user}")
        
        # Test 4: List tables
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            ORDER BY table_name;
        """)
        tables = cursor.fetchall()
        
        print(f"📋 Tables Available: {len(tables)}")
        if tables:
            print("   Sample tables:")
            for table in tables[:10]:  # Show first 10 tables
                print(f"   • {table[0]}")
            if len(tables) > 10:
                print(f"   ... and {len(tables) - 10} more tables")
        else:
            print("   ⚠️  No tables found - Need to run Django migrations")
        
        # Test 5: Check if Django tables exist
        django_tables = [t[0] for t in tables if 'auth_' in t[0] or 'django_' in t[0]]
        if django_tables:
            print(f"✅ Django Tables: {len(django_tables)} found")
            print(f"   Example: {django_tables[0]}")
        else:
            print("⚠️  Django Tables: None found")
        
        # Test 6: Check custom app tables
        custom_tables = [t[0] for t in tables if any(prefix in t[0] for prefix in ['accounts_', 'course_', 'core_'])]
        if custom_tables:
            print(f"✅ Custom App Tables: {len(custom_tables)} found")
            for table in custom_tables[:5]:
                print(f"   • {table}")
        else:
            print("⚠️  Custom App Tables: None found")
        
        print()
        print("🎉 DATABASE TEST RESULTS:")
        print("=" * 30)
        print("✅ Connection: Working perfectly")
        print("✅ Authentication: Successful")
        print("✅ Query execution: Functional")
        print(f"✅ Tables: {len(tables)} available")
        
        # Close connection
        cursor.close()
        conn.close()
        
        print()
        print("🔧 RECOMMENDATION:")
        if tables:
            print("✅ Database is ready for Django!")
            print("✅ SavvyIndians LMS can now use dynamic database features")
            print("🎯 Next: Fix Django serverless initialization")
        else:
            print("⚠️  Run Django migrations to create tables:")
            print("   python manage.py migrate")
        
        return True
        
    except Exception as e:
        print("❌ DATABASE CONNECTION FAILED!")
        print(f"🚨 Error: {e}")
        print()
        print("🔧 TROUBLESHOOTING:")
        print("1. Check internet connectivity")
        print("2. Verify Neon database is active")
        print("3. Check firewall settings")
        print("4. Verify connection string format")
        print("5. Ensure psycopg2 is installed")
        
        return False
    
    finally:
        print()
        print("=" * 60)

if __name__ == "__main__":
    success = test_postgresql_direct()
    
    if success:
        print("✅ NEXT STEPS:")
        print("1. Fix Django serverless initialization issue")
        print("2. Test Django database queries in Vercel")
        print("3. Enable full SavvyIndians LMS features")
    else:
        print("🔧 REQUIRED FIXES:")
        print("1. Fix database connection issues")
        print("2. Install required packages")
        print("3. Verify Neon database status")