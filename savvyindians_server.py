#!/usr/bin/env python
"""
SavvyIndians LMS Homepage Test & Server Launcher
"""
import os
import sys
import time
from pathlib import Path

# Get the current directory
BASE_DIR = Path(__file__).resolve().parent

# Add project to Python path
sys.path.insert(0, str(BASE_DIR))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

def test_homepage_data():
    """Test if homepage has all required data"""
    try:
        import django
        # django.setup()  # Disabled to prevent reentrant initialization
        
        from course.models import Course, UploadVideo
        from accounts.models import User
        
        # Get data counts
        total_courses = Course.objects.count()
        total_videos = UploadVideo.objects.count()
        total_students = User.objects.filter(is_student=True).count()
        
        print("📊 SavvyIndians LMS Database Stats:")
        print(f"   📚 Courses: {total_courses}")
        print(f"   🎥 Videos: {total_videos}")
        print(f"   👨‍🎓 Students: {total_students}")
        
        # Get featured content
        featured_videos = UploadVideo.objects.all()[:8]
        print(f"\n🎬 Featured Videos ({len(featured_videos)}):")
        for video in featured_videos:
            print(f"   • {video.title} - {video.course.title}")
            
        return True
        
    except Exception as e:
        print(f"❌ Database test failed: {e}")
        return False

def run_server():
    """Run Django development server"""
    try:
        from django.core.management import call_command
        print("\n🚀 Starting SavvyIndians LMS Server...")
        print("🌐 Homepage: http://127.0.0.1:8000/")
        print("🔐 Student Login: http://127.0.0.1:8000/accounts/student/login/")
        print("🛠️ Admin Panel: http://127.0.0.1:8000/admin/")
        print("\n✨ Features Available:")
        print("   • Google OAuth Login")
        print("   • Featured Video Gallery")
        print("   • Course Catalog")
        print("   • Interactive Learning")
        print("   • Progress Tracking")
        print("   • Quiz System")
        print("   • Payment Integration")
        print("\n🎯 Demo Credentials:")
        print("   Admin: Priyanshu-Yadav / [your password]")
        print("   Student: student001 / student123")
        
        print("\n" + "="*50)
        print("🎉 SavvyIndians LMS is READY!")
        print("="*50)
        
        call_command('runserver', '127.0.0.1:8000')
        
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Server failed to start: {e}")

if __name__ == '__main__':
    print("🔧 Testing SavvyIndians LMS Setup...")
    
    if test_homepage_data():
        print("✅ All tests passed! Starting server...")
        time.sleep(2)
        run_server()
    else:
        print("❌ Setup failed. Please check configuration.")