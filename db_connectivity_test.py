#!/usr/bin/env python
"""
🔍 SAVVYINDIANS LMS - DATABASE CONNECTIVITY TEST
===============================================
Test database connections and diagnose issues
"""

import requests
import json

def test_database_connectivity():
    """Test the database connectivity via the web endpoint"""
    
    print("🔍 SAVVYINDIANS LMS - DATABASE CONNECTIVITY TEST")
    print("=" * 60)
    print()
    
    # Test URLs
    base_url = "https://django-lms-main-azuzm2i31-gy068644-8794s-projects.vercel.app"
    db_test_url = f"{base_url}/db-test/"
    homepage_url = base_url
    
    print("🌐 Testing Database Connection...")
    print(f"🔗 Database Test URL: {db_test_url}")
    print()
    
    try:
        # Test database endpoint
        print("⏳ Connecting to database test endpoint...")
        response = requests.get(db_test_url, timeout=30)
        
        print(f"📊 Status Code: {response.status_code}")
        print(f"⏱️  Response Time: {response.elapsed.total_seconds():.2f}s")
        print()
        
        if response.status_code == 200:
            try:
                data = response.json()
                print("✅ DATABASE TEST RESULTS:")
                print("-" * 30)
                
                if data.get("status") == "success":
                    print("🎉 DATABASE CONNECTION: SUCCESS!")
                    print(f"👥 User Count: {data.get('user_count', 'Unknown')}")
                    print(f"👨‍💼 Group Count: {data.get('group_count', 'Unknown')}")
                    print(f"📚 Course Count: {data.get('course_count', 'Not available')}")
                    print(f"🗄️  Database Engine: {data.get('database_engine', 'Unknown')}")
                    print(f"🏠 Database Name: {data.get('database_name', 'Unknown')}")
                    print()
                    print("✅ VERDICT: Database is working perfectly!")
                    
                elif data.get("status") == "error":
                    print("❌ DATABASE CONNECTION: FAILED!")
                    print(f"🚨 Error: {data.get('error', 'Unknown error')}")
                    print()
                    print("🔧 DATABASE SETTINGS:")
                    db_settings = data.get('database_settings', {})
                    for key, value in db_settings.items():
                        print(f"   {key}: {value}")
                    print()
                    print("🛠️  TROUBLESHOOTING STEPS:")
                    print("1. Check Vercel environment variables")
                    print("2. Verify DATABASE_URL format")
                    print("3. Test Neon database connection")
                    print("4. Check firewall/network settings")
                    
            except json.JSONDecodeError:
                print("⚠️  Response is not JSON. Raw response:")
                print(response.text[:500] + "..." if len(response.text) > 500 else response.text)
                
        elif response.status_code == 500:
            print("❌ INTERNAL SERVER ERROR (500)")
            print("🔧 This usually means Django/database configuration issue")
            try:
                data = response.json()
                print(f"🚨 Error Details: {data.get('error', 'Unknown')}")
            except:
                print("Raw error response:")
                print(response.text[:200] + "..." if len(response.text) > 200 else response.text)
                
        else:
            print(f"⚠️  Unexpected status code: {response.status_code}")
            print("Response preview:")
            print(response.text[:200] + "..." if len(response.text) > 200 else response.text)
    
    except requests.exceptions.Timeout:
        print("⏳ TIMEOUT ERROR")
        print("Database query took too long (>30 seconds)")
        print("This might indicate:")
        print("• Database connection issues")
        print("• Slow query performance")
        print("• Network connectivity problems")
        
    except requests.exceptions.RequestException as e:
        print(f"🌐 CONNECTION ERROR: {e}")
        print("This might indicate:")
        print("• DNS resolution issues")
        print("• Network connectivity problems")
        print("• Vercel deployment issues")
    
    print()
    print("🌐 Testing Homepage Status...")
    try:
        response = requests.get(homepage_url, timeout=10)
        if response.status_code == 200:
            if "Database Connected" in response.text:
                print("✅ Homepage shows: Database Connected")
            elif "Static Mode" in response.text:
                print("⚠️  Homepage shows: Static Mode (Database issue)")
            else:
                print("ℹ️  Homepage loaded but database status unclear")
        else:
            print(f"❌ Homepage error: {response.status_code}")
    except Exception as e:
        print(f"❌ Homepage test failed: {e}")
    
    print()
    print("📋 QUICK DIAGNOSIS:")
    print("=" * 20)
    print("If database test succeeds: ✅ Database is working")
    print("If database test fails: ❌ Need to fix configuration")
    print("If homepage shows 'Static Mode': ⚠️  Database connection issues")
    print()
    print("🔧 NEXT STEPS BASED ON RESULTS:")
    print("✅ Success → Test authentication and add content")
    print("❌ Error → Fix environment variables and database config")
    print("⚠️  Partial → Debug specific connection issues")
    print()
    print("=" * 60)

if __name__ == "__main__":
    test_database_connectivity()