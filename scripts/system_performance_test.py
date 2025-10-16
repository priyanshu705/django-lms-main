#!/usr/bin/env python
"""
System Performance and Integration Test
Tests all major components working together
"""

import os
import sys
import django
import time
from datetime import datetime

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from accounts.models import User, Student
from course.models import Course, Program, UploadVideo, VideoProgress
from core.models import Session, Semester
from django.test import Client
from django.urls import reverse

def test_database_performance():
    """Test database queries and performance"""
    
    print("💾 Testing Database Performance")
    print("=" * 35)
    
    start_time = time.time()
    
    # Test data counts
    tests = [
        ("Users", User.objects.count()),
        ("Students", Student.objects.count()),
        ("Programs", Program.objects.count()),
        ("Courses", Course.objects.count()),
        ("Videos", UploadVideo.objects.count()),
        ("Progress Records", VideoProgress.objects.count()),
        ("Sessions", Session.objects.count()),
        ("Semesters", Semester.objects.count()),
    ]
    
    for name, count in tests:
        print(f"   {name}: {count}")
    
    # Test complex queries
    print("\n🔍 Complex Query Tests:")
    
    # Students with progress
    start = time.time()
    students_with_progress = Student.objects.filter(
        student__videoprogress__isnull=False
    ).distinct().count()
    query_time = (time.time() - start) * 1000
    print(f"   Students with progress: {students_with_progress} ({query_time:.2f}ms)")
    
    # Average progress per course
    start = time.time()
    courses_with_avg_progress = []
    for course in Course.objects.all():
        videos = course.uploadvideo_set.all()
        if videos:
            total_progress = sum(
                VideoProgress.objects.filter(video__in=videos).values_list('completion_percentage', flat=True)
            )
            video_count = VideoProgress.objects.filter(video__in=videos).count()
            avg_progress = total_progress / video_count if video_count > 0 else 0
            courses_with_avg_progress.append((course.title, avg_progress))
    
    query_time = (time.time() - start) * 1000
    print(f"   Course progress calculated: {len(courses_with_avg_progress)} courses ({query_time:.2f}ms)")
    
    total_time = (time.time() - start_time) * 1000
    print(f"\n✅ Database tests completed in {total_time:.2f}ms")
    
    return total_time < 1000  # Should complete under 1 second

def test_web_interface():
    """Test web interface responses"""
    
    print("\n🌐 Testing Web Interface")
    print("=" * 25)
    
    client = Client()
    success = True
    
    # Test pages
    test_urls = [
        ('/', 'Homepage'),
        ('/en/', 'Localized Homepage'),
        ('/accounts/student/login/', 'Student Login'),
        ('/admin/', 'Admin Panel'),
    ]
    
    for url, name in test_urls:
        try:
            start = time.time()
            response = client.get(url)
            response_time = (time.time() - start) * 1000
            
            if response.status_code in [200, 302]:  # 302 for redirects
                print(f"   ✅ {name}: {response.status_code} ({response_time:.2f}ms)")
            else:
                print(f"   ❌ {name}: {response.status_code} ({response_time:.2f}ms)")
                success = False
                
        except Exception as e:
            print(f"   ❌ {name}: Error - {str(e)}")
            success = False
    
    # Test student login
    try:
        start = time.time()
        response = client.post('/accounts/student/login/', {
            'username': 'alice_johnson',
            'password': 'testpass123'
        })
        response_time = (time.time() - start) * 1000
        
        if response.status_code in [200, 302]:
            print(f"   ✅ Student Login POST: {response.status_code} ({response_time:.2f}ms)")
        else:
            print(f"   ❌ Student Login POST: {response.status_code} ({response_time:.2f}ms)")
            success = False
            
    except Exception as e:
        print(f"   ❌ Student Login POST: Error - {str(e)}")
        success = False
    
    return success

def test_video_integration():
    """Test YouTube video integration"""
    
    print("\n🎬 Testing Video Integration")
    print("=" * 30)
    
    success = True
    
    # Test video URL processing
    youtube_videos = UploadVideo.objects.filter(is_youtube_video=True)[:3]
    
    for video in youtube_videos:
        try:
            # Test URL extraction
            video_id = video.get_youtube_video_id()
            embed_url = video.get_youtube_embed_url()
            
            if video_id and embed_url:
                print(f"   ✅ {video.title}: ID={video_id}")
            else:
                print(f"   ❌ {video.title}: URL processing failed")
                success = False
                
        except Exception as e:
            print(f"   ❌ {video.title}: Error - {str(e)}")
            success = False
    
    print(f"   📊 Total YouTube videos: {youtube_videos.count()}")
    return success

def test_progress_system():
    """Test progress tracking system"""
    
    print("\n📈 Testing Progress System")
    print("=" * 28)
    
    success = True
    
    try:
        # Test progress calculations
        progress_records = VideoProgress.objects.all()[:5]
        
        for progress in progress_records:
            # Test percentage calculation
            expected_percentage = (progress.watch_time / progress.total_duration * 100) if progress.total_duration > 0 else 0
            expected_percentage = min(expected_percentage, 100.0)
            
            if abs(progress.completion_percentage - expected_percentage) < 0.1:
                print(f"   ✅ {progress.student.username} - {progress.video.title}: {progress.completion_percentage:.1f}%")
            else:
                print(f"   ❌ {progress.student.username} - {progress.video.title}: Calculation error")
                success = False
        
        # Test completion logic
        completed_count = progress_records.filter(is_completed=True).count()
        print(f"   📊 Completed videos: {completed_count}/{progress_records.count()}")
        
    except Exception as e:
        print(f"   ❌ Progress system error: {str(e)}")
        success = False
    
    return success

def generate_system_report():
    """Generate comprehensive system status report"""
    
    print("\n📋 System Status Report")
    print("=" * 25)
    
    # System stats
    stats = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'total_users': User.objects.count(),
        'active_students': User.objects.filter(is_student=True).count(),
        'total_courses': Course.objects.count(),
        'total_videos': UploadVideo.objects.count(),
        'youtube_videos': UploadVideo.objects.filter(is_youtube_video=True).count(),
        'progress_records': VideoProgress.objects.count(),
        'completed_videos': VideoProgress.objects.filter(is_completed=True).count(),
    }
    
    # Calculate engagement metrics
    if stats['progress_records'] > 0:
        avg_completion = VideoProgress.objects.aggregate(
            models.Avg('completion_percentage')
        )['completion_percentage__avg'] or 0
        stats['avg_completion_rate'] = f"{avg_completion:.1f}%"
        
        completion_rate = (stats['completed_videos'] / stats['progress_records']) * 100
        stats['video_completion_rate'] = f"{completion_rate:.1f}%"
    else:
        stats['avg_completion_rate'] = "0%"
        stats['video_completion_rate'] = "0%"
    
    # Print report
    print(f"   🕐 Generated: {stats['timestamp']}")
    print(f"   👥 Total Users: {stats['total_users']}")
    print(f"   🎓 Active Students: {stats['active_students']}")
    print(f"   📚 Courses: {stats['total_courses']}")
    print(f"   🎬 Videos: {stats['total_videos']} ({stats['youtube_videos']} YouTube)")
    print(f"   📈 Progress Records: {stats['progress_records']}")
    print(f"   ✅ Completed Videos: {stats['completed_videos']}")
    print(f"   📊 Average Completion: {stats['avg_completion_rate']}")
    print(f"   🎯 Video Completion Rate: {stats['video_completion_rate']}")
    
    return stats

def main():
    """Main system test function"""
    
    print("🔧 Django LMS System Performance Test")
    print("=" * 45)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    overall_start = time.time()
    
    # Run all tests
    tests = [
        ("Database Performance", test_database_performance),
        ("Web Interface", test_web_interface), 
        ("Video Integration", test_video_integration),
        ("Progress System", test_progress_system),
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        try:
            start = time.time()
            result = test_func()
            duration = time.time() - start
            results[test_name] = {
                'success': result,
                'duration': duration * 1000
            }
        except Exception as e:
            results[test_name] = {
                'success': False,
                'duration': 0,
                'error': str(e)
            }
    
    # Generate report
    system_stats = generate_system_report()
    
    # Summary
    total_time = (time.time() - overall_start) * 1000
    
    print(f"\n🏁 Test Summary")
    print("=" * 15)
    
    passed = sum(1 for r in results.values() if r['success'])
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result['success'] else "❌ FAIL"
        duration = result['duration']
        print(f"   {status} {test_name}: {duration:.2f}ms")
        
        if not result['success'] and 'error' in result:
            print(f"       Error: {result['error']}")
    
    print(f"\n   📊 Results: {passed}/{total} tests passed")
    print(f"   ⏱ Total Time: {total_time:.2f}ms")
    
    if passed == total:
        print("\n🎉 All tests passed! System is performing excellently.")
        print("✅ Ready for production deployment!")
    else:
        print(f"\n⚠ {total-passed} test(s) failed. Please review the issues above.")
    
    return passed == total

if __name__ == '__main__':
    # Import models for aggregation
    from django.db import models
    
    success = main()
    sys.exit(0 if success else 1)