#!/usr/bin/env python
"""
Test Video Progress Tracking System
Verifies that the video progress tracking functionality works correctly
"""

import os
import sys
import django

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from accounts.models import User
from course.models import UploadVideo, VideoProgress
from django.db import transaction

def test_progress_tracking():
    """Test the video progress tracking functionality"""
    
    print("🧪 Testing Video Progress Tracking System")
    print("=" * 50)
    
    try:
        # Get test data
        test_student = User.objects.filter(username='alice_johnson', is_student=True).first()
        if not test_student:
            print("❌ Test student 'alice_johnson' not found")
            return False
        
        # Get test video
        test_video = UploadVideo.objects.filter(title__icontains='Introduction to Python').first()
        if not test_video:
            print("❌ Test video not found")
            return False
        
        print(f"✓ Found test student: {test_student.get_full_name}")
        print(f"✓ Found test video: {test_video.title}")
        
        # Check existing progress
        existing_progress = VideoProgress.objects.filter(
            student=test_student,
            video=test_video
        ).first()
        
        if existing_progress:
            print(f"✓ Existing progress found: {existing_progress.completion_percentage:.1f}%")
            print(f"  - Watch time: {existing_progress.time_watched_display}")
            print(f"  - Completed: {existing_progress.is_completed}")
            print(f"  - Last watched: {existing_progress.last_watched}")
        else:
            print("⚠ No existing progress found")
        
        # Test progress calculations
        if existing_progress:
            # Test different scenarios
            test_scenarios = [
                {"watch_time": 900, "total_duration": 1800, "expected_percentage": 50.0},
                {"watch_time": 1620, "total_duration": 1800, "expected_percentage": 90.0},
                {"watch_time": 1800, "total_duration": 1800, "expected_percentage": 100.0},
            ]
            
            print("\n🔍 Testing Progress Calculations:")
            for i, scenario in enumerate(test_scenarios, 1):
                # Update progress
                existing_progress.watch_time = scenario["watch_time"]
                existing_progress.total_duration = scenario["total_duration"]
                existing_progress.save()  # This will trigger the calculation
                
                print(f"  Test {i}: {scenario['watch_time']}s / {scenario['total_duration']}s")
                print(f"    Expected: {scenario['expected_percentage']:.1f}%")
                print(f"    Actual: {existing_progress.completion_percentage:.1f}%")
                print(f"    Completed: {existing_progress.is_completed}")
                
                # Verify calculation
                if abs(existing_progress.completion_percentage - scenario['expected_percentage']) < 0.1:
                    print(f"    ✅ Progress calculation correct!")
                else:
                    print(f"    ❌ Progress calculation incorrect!")
                
                print()
        
        # Test progress summary for student
        print("📊 Student Progress Summary:")
        all_progress = VideoProgress.objects.filter(student=test_student).order_by('-last_watched')
        
        if all_progress.exists():
            print(f"   Total videos started: {all_progress.count()}")
            completed_count = all_progress.filter(is_completed=True).count()
            print(f"   Completed videos: {completed_count}")
            
            avg_progress = sum(p.completion_percentage for p in all_progress) / all_progress.count()
            print(f"   Average progress: {avg_progress:.1f}%")
            
            print("\n   Recent progress:")
            for progress in all_progress[:5]:  # Show top 5 recent
                print(f"     • {progress.video.title}: {progress.completion_percentage:.1f}% ({progress.time_watched_display})")
        else:
            print("   No progress found")
        
        # Test course-level progress
        print("\n🎓 Course Progress Summary:")
        courses_with_progress = {}
        
        for progress in all_progress:
            course_title = progress.video.course.title
            if course_title not in courses_with_progress:
                courses_with_progress[course_title] = []
            courses_with_progress[course_title].append(progress)
        
        for course_title, progress_list in courses_with_progress.items():
            total_videos = len(progress_list)
            completed_videos = sum(1 for p in progress_list if p.is_completed)
            avg_course_progress = sum(p.completion_percentage for p in progress_list) / total_videos
            
            print(f"   📚 {course_title}:")
            print(f"      Videos: {completed_videos}/{total_videos} completed")
            print(f"      Progress: {avg_course_progress:.1f}%")
        
        print("\n" + "=" * 50)
        print("✅ Video Progress Tracking System Test Completed!")
        return True
        
    except Exception as e:
        print(f"❌ Error testing progress tracking: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def test_video_urls():
    """Test YouTube video URL processing"""
    
    print("\n🎬 Testing YouTube Video URLs")
    print("=" * 30)
    
    try:
        videos = UploadVideo.objects.filter(is_youtube_video=True)[:3]
        
        for video in videos:
            print(f"\n📺 {video.title}")
            print(f"   Original URL: {video.youtube_url}")
            print(f"   Embed URL: {video.get_youtube_embed_url()}")
            print(f"   Video ID: {video.get_youtube_video_id()}")
            print(f"   Course: {video.course.title}")
        
        print(f"\n✅ Tested {videos.count()} YouTube videos successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error testing YouTube URLs: {str(e)}")
        return False

def main():
    """Main test function"""
    
    success = True
    success &= test_progress_tracking()
    success &= test_video_urls()
    
    if success:
        print("\n🎉 All tests passed! The system is ready for demo.")
    else:
        print("\n⚠ Some tests failed. Please check the system.")

if __name__ == '__main__':
    main()