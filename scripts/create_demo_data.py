#!/usr/bin/env python
"""
Demo Data Generation Script for Django LMS
Creates test student accounts and sample video courses for demonstration
"""

import os
import sys
import django
from datetime import datetime, timedelta
from django.utils import timezone

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from accounts.models import User, Student
from course.models import Course, Program, UploadVideo, VideoProgress
from core.models import Session, Semester
from django.db import transaction

def create_test_students():
    """Create diverse test student accounts"""
    
    students_data = [
        {
            'username': 'alice_johnson',
            'email': 'alice@example.com',
            'first_name': 'Alice',
            'last_name': 'Johnson',
            'password': 'testpass123',
            'level': 'beginner'
        },
        {
            'username': 'bob_smith',
            'email': 'bob@example.com',
            'first_name': 'Bob',
            'last_name': 'Smith',
            'password': 'testpass123',
            'level': 'intermediate'
        },
        {
            'username': 'carol_davis',
            'email': 'carol@example.com',
            'first_name': 'Carol',
            'last_name': 'Davis',
            'password': 'testpass123',
            'level': 'advanced'
        },
        {
            'username': 'david_wilson',
            'email': 'david@example.com',
            'first_name': 'David',
            'last_name': 'Wilson',
            'password': 'testpass123',
            'level': 'beginner'
        },
        {
            'username': 'emma_brown',
            'email': 'emma@example.com',
            'first_name': 'Emma',
            'last_name': 'Brown',
            'password': 'testpass123',
            'level': 'intermediate'
        }
    ]
    
    created_students = []
    
    for student_data in students_data:
        # Check if user already exists
        if User.objects.filter(username=student_data['username']).exists():
            print(f"✓ Student {student_data['username']} already exists")
            user = User.objects.get(username=student_data['username'])
        else:
            # Create user account without triggering signals
            user = User(
                username=student_data['username'],
                email=student_data['email'],
                first_name=student_data['first_name'],
                last_name=student_data['last_name'],
                is_student=True,
                is_active=True
            )
            user.set_password(student_data['password'])
            
            # Temporarily disconnect signals to avoid auto-generation issues
            from django.db.models.signals import post_save
            from accounts.signals import post_save_account_receiver
            
            post_save.disconnect(post_save_account_receiver, sender=User)
            user.save()
            post_save.connect(post_save_account_receiver, sender=User)
            
            print(f"✓ Created user: {student_data['username']}")
        
        # Create or get student profile
        student, created = Student.objects.get_or_create(
            student=user,
            defaults={
                'level': student_data['level'].title() + ' Degree'  # Convert to match LEVEL choices
            }
        )
        
        if created:
            print(f"✓ Created student profile for: {student_data['username']}")
        else:
            print(f"✓ Student profile already exists for: {student_data['username']}")
            
        created_students.append(student)
    
    return created_students

def create_programs():
    """Create sample programs"""
    
    programs_data = [
        {'title': 'Computer Science Program', 'summary': 'Comprehensive computer science curriculum covering programming, algorithms, and software development'},
        {'title': 'Web Development Program', 'summary': 'Full-stack web development training with modern frameworks and technologies'},
        {'title': 'Data Science Program', 'summary': 'Data analysis, machine learning, and statistical modeling comprehensive course'},
        {'title': 'Mobile Development Program', 'summary': 'Cross-platform mobile app development for iOS and Android'},
        {'title': 'DevOps Engineering Program', 'summary': 'Infrastructure automation, deployment, and cloud technologies mastery'}
    ]
    
    created_programs = []
    
    for program_data in programs_data:
        program, created = Program.objects.get_or_create(
            title=program_data['title'],
            defaults={
                'summary': program_data['summary']
            }
        )
        
        if created:
            print(f"✓ Created program: {program_data['title']}")
        else:
            print(f"✓ Program already exists: {program_data['title']}")
            
        created_programs.append(program)
    
    return created_programs

def create_sample_courses(programs):
    """Create comprehensive sample courses with YouTube videos"""
    
    courses_data = [
        {
            'title': 'Python Programming Fundamentals',
            'code': 'CS101',
            'program': 'Computer Science Program',
            'summary': 'Master Python programming from basics to advanced concepts. Perfect for beginners starting their coding journey.',
            'credit': 3,
            'videos': [
                {
                    'title': 'Introduction to Python',
                    'youtube_url': 'https://www.youtube.com/watch?v=kqtD5dpn9C8',  # Python tutorial
                    'summary': 'Learn what Python is and why it\'s so popular in programming.',
                },
                {
                    'title': 'Variables and Data Types',
                    'youtube_url': 'https://www.youtube.com/watch?v=cQT33yu9pY8',  # Variables tutorial
                    'summary': 'Understand different data types and how to work with variables.',
                },
                {
                    'title': 'Control Structures',
                    'youtube_url': 'https://www.youtube.com/watch?v=DZwmZ8Usvnk',  # Control structures
                    'summary': 'Master if statements, loops, and conditional logic.',
                },
                {
                    'title': 'Functions and Modules',
                    'youtube_url': 'https://www.youtube.com/watch?v=9Os0o3wzS_I',  # Functions tutorial
                    'summary': 'Learn to create reusable code with functions and modules.',
                }
            ]
        },
        {
            'title': 'Web Development with Django',
            'code': 'WEB201',
            'program': 'Web Development Program',
            'summary': 'Build powerful web applications using Django framework. Learn from project setup to deployment.',
            'credit': 4,
            'videos': [
                {
                    'title': 'Django Introduction',
                    'youtube_url': 'https://www.youtube.com/watch?v=F5mRW0jo-U4',  # Django intro
                    'summary': 'Get started with Django web framework basics.',
                },
                {
                    'title': 'Models and Database',
                    'youtube_url': 'https://www.youtube.com/watch?v=rHux0gMZ3Eg',  # Django models
                    'summary': 'Design database models and work with Django ORM.',
                },
                {
                    'title': 'Views and Templates',
                    'youtube_url': 'https://www.youtube.com/watch?v=06w7n3tAM6Y',  # Views and templates
                    'summary': 'Create dynamic web pages with views and templates.',
                }
            ]
        },
        {
            'title': 'Data Science with Python',
            'code': 'DS301',
            'program': 'Data Science Program',
            'summary': 'Explore data analysis, visualization, and machine learning using Python libraries.',
            'credit': 4,
            'videos': [
                {
                    'title': 'NumPy and Pandas Basics',
                    'youtube_url': 'https://www.youtube.com/watch?v=ZyhVh-qRZPA',  # NumPy Pandas
                    'summary': 'Master data manipulation with NumPy and Pandas.',
                },
                {
                    'title': 'Data Visualization',
                    'youtube_url': 'https://www.youtube.com/watch?v=a9UrKTVEeZA',  # Data visualization
                    'summary': 'Create stunning visualizations with Matplotlib and Seaborn.',
                },
                {
                    'title': 'Machine Learning Basics',
                    'youtube_url': 'https://www.youtube.com/watch?v=7eh4d6sabA0',  # ML basics
                    'summary': 'Introduction to machine learning concepts and algorithms.',
                }
            ]
        },
        {
            'title': 'React Native Mobile Development',
            'code': 'MOB401',
            'program': 'Mobile Development Program',
            'summary': 'Build cross-platform mobile apps using React Native framework.',
            'credit': 3,
            'videos': [
                {
                    'title': 'React Native Setup',
                    'youtube_url': 'https://www.youtube.com/watch?v=0-S5a0eXPoc',  # React Native setup
                    'summary': 'Set up your development environment for React Native.',
                },
                {
                    'title': 'Components and Navigation',
                    'youtube_url': 'https://www.youtube.com/watch?v=Hf4MJH0jDb4',  # Components
                    'summary': 'Learn React Native components and navigation.',
                }
            ]
        },
        {
            'title': 'DevOps with Docker and Kubernetes',
            'code': 'DEV501',
            'program': 'DevOps Engineering Program',
            'summary': 'Master containerization and orchestration for modern application deployment.',
            'credit': 4,
            'videos': [
                {
                    'title': 'Docker Fundamentals',
                    'youtube_url': 'https://www.youtube.com/watch?v=3c-iBn73dDE',  # Docker basics
                    'summary': 'Learn containerization with Docker from scratch.',
                },
                {
                    'title': 'Kubernetes Introduction',
                    'youtube_url': 'https://www.youtube.com/watch?v=X48VuDVv0do',  # Kubernetes intro
                    'summary': 'Orchestrate containers with Kubernetes.',
                }
            ]
        }
    ]
    
    created_courses = []
    
    for course_data in courses_data:
        # Find the program
        program = next((p for p in programs if p.title == course_data['program']), None)
        if not program:
            print(f"⚠ Program not found: {course_data['program']}")
            continue
        
        # Create or get course
        course, created = Course.objects.get_or_create(
            code=course_data['code'],
            defaults={
                'title': course_data['title'],
                'program': program,
                'summary': course_data['summary'],
                'credit': course_data['credit'],
                'level': 'Bachelor',
                'year': 1,
                'semester': 'First',
                'is_elective': False
            }
        )
        
        if created:
            print(f"✓ Created course: {course_data['title']}")
        else:
            print(f"✓ Course already exists: {course_data['title']}")
        
        # Create videos
        for video_data in course_data['videos']:
            video, video_created = UploadVideo.objects.get_or_create(
                course=course,
                title=video_data['title'],
                defaults={
                    'youtube_url': video_data['youtube_url'],
                    'summary': video_data['summary'],
                    'is_youtube_video': True
                }
            )
            
            if video_created:
                print(f"  ✓ Created video: {video_data['title']}")
            else:
                print(f"  ✓ Video already exists: {video_data['title']}")
        
        created_courses.append(course)
    
    return created_courses

def create_sample_progress(students, courses):
    """Create sample video progress for testing"""
    
    import random
    
    progress_scenarios = [
        # Alice - Active learner with mixed progress
        {
            'student': 0,  # Alice
            'courses': [0, 1],  # Python and Django
            'progress_pattern': 'active'
        },
        # Bob - Completed one course, started another
        {
            'student': 1,  # Bob
            'courses': [0, 2],  # Python and Data Science
            'progress_pattern': 'completed'
        },
        # Carol - Advanced learner, multiple courses
        {
            'student': 2,  # Carol
            'courses': [1, 3, 4],  # Django, React Native, DevOps
            'progress_pattern': 'advanced'
        },
        # David - New student, just started
        {
            'student': 3,  # David
            'courses': [0],  # Python only
            'progress_pattern': 'beginner'
        },
        # Emma - Intermediate progress
        {
            'student': 4,  # Emma
            'courses': [2, 3],  # Data Science, React Native
            'progress_pattern': 'intermediate'
        }
    ]
    
    for scenario in progress_scenarios:
        student = students[scenario['student']]
        student_courses = [courses[i] for i in scenario['courses'] if i < len(courses)]
        
        for course in student_courses:
            videos = course.uploadvideo_set.all()  # Get related videos
            
            for i, video in enumerate(videos):
                # Calculate progress based on pattern
                progress = _calculate_progress(scenario['progress_pattern'], i, len(videos), course, student_courses)
                
                if progress > 0:
                    # Estimated video duration (30 minutes default)
                    total_duration = 1800  # 30 minutes in seconds
                    watch_time = int(total_duration * progress)
                    is_completed = progress >= 0.9
                    
                    _, created = VideoProgress.objects.get_or_create(
                        student=student.student,  # Use the User object
                        video=video,
                        defaults={
                            'watch_time': watch_time,
                            'total_duration': total_duration,
                            'completion_percentage': progress * 100,
                            'is_completed': is_completed,
                            'last_position': watch_time
                        }
                    )
                    
                    if created:
                        print(f"  ✓ Created progress: {student.student.username} - {video.title} ({progress*100:.1f}%)")

def _calculate_progress(pattern, video_index, total_videos, course, student_courses):
    """Calculate progress percentage based on learning pattern"""
    import random
    
    if pattern == 'active':
        # Mixed progress - some completed, some partial
        if video_index < total_videos // 2:
            return random.uniform(0.8, 1.0)
        else:
            return random.uniform(0.2, 0.7)
    elif pattern == 'completed':
        # First course completed, second started
        if course == student_courses[0]:
            return 1.0
        else:
            return random.uniform(0.1, 0.4) if video_index < 2 else 0.0
    elif pattern == 'advanced':
        # High progress across multiple courses
        return random.uniform(0.6, 1.0)
    elif pattern == 'beginner':
        # Just started, low progress
        if video_index == 0:
            return random.uniform(0.3, 0.6)
        else:
            return 0.0
    elif pattern == 'intermediate':
        # Steady progress
        return random.uniform(0.4, 0.8)
    else:
        return 0.0

def create_session_and_semester():
    """Create session and semester required for courses"""
    
    # Create session
    session, created = Session.objects.get_or_create(
        session='2024/2025',
        defaults={
            'is_current_session': True,
            'next_session_begins': timezone.now().date()
        }
    )
    
    if created:
        print("✓ Created session: 2024/2025")
    else:
        print("✓ Session already exists: 2024/2025")
    
    # Create semester
    semester, created = Semester.objects.get_or_create(
        semester='First',
        defaults={
            'is_current_semester': True,
            'session': session,
            'next_semester_begins': timezone.now().date()
        }
    )
    
    if created:
        print("✓ Created semester: First")
    else:
        print("✓ Semester already exists: First")
    
    return session, semester

def create_admin_user():
    """Create admin user if it doesn't exist"""
    
    admin_data = {
        'username': 'admin',
        'email': 'admin@example.com',
        'password': 'admin123',
        'first_name': 'Admin',
        'last_name': 'User'
    }
    
    if User.objects.filter(username=admin_data['username']).exists():
        print("✓ Admin user already exists")
        return User.objects.get(username=admin_data['username'])
    
    admin_user = User.objects.create_superuser(
        username=admin_data['username'],
        email=admin_data['email'],
        password=admin_data['password'],
        first_name=admin_data['first_name'],
        last_name=admin_data['last_name']
    )
    
    print(f"✓ Created admin user: {admin_data['username']}")
    return admin_user

def main():
    """Main function to create all demo data"""
    
    print("🚀 Creating Demo Data for Django LMS")
    print("=" * 50)
    
    try:
        with transaction.atomic():
            # Create session and semester first
            print("\n📅 Creating Session and Semester...")
            create_session_and_semester()
            
            # Create admin user
            print("\n📝 Creating Admin User...")
            create_admin_user()
            
            # Create test students
            print("\n👥 Creating Test Student Accounts...")
            students = create_test_students()
            
            # Create programs
            print("\n📚 Creating Programs...")
            programs = create_programs()
            
            # Create sample courses
            print("\n🎓 Creating Sample Courses...")
            courses = create_sample_courses(programs)
            
            # Create sample progress
            print("\n📈 Creating Sample Progress Data...")
            create_sample_progress(students, courses)
            
            print("\n" + "=" * 50)
            print("✅ Demo data creation completed successfully!")
            print("\n📊 Summary:")
            print(f"   • {len(students)} test students created")
            print(f"   • {len(programs)} programs created")
            print(f"   • {len(courses)} courses created")
            print("   • 1 admin user created")
            print("   • Progress data generated for realistic testing")
            
            print("\n🔐 Login Credentials:")
            print("   👨‍💼 Admin: username='admin', password='admin123'")
            print("   👨‍🎓 Students: username='alice_johnson', password='testpass123'")
            print("   👨‍🎓           username='bob_smith', password='testpass123'")
            print("   👩‍🎓           username='carol_davis', password='testpass123'")
            print("   👨‍🎓           username='david_wilson', password='testpass123'")
            print("   👩‍🎓           username='emma_brown', password='testpass123'")
            
            print("\n🌐 Next Steps:")
            print("   1. Start the server: python manage.py runserver")
            print("   2. Visit: http://127.0.0.1:8001")
            print("   3. Test student login and course navigation")
            print("   4. Check admin panel: http://127.0.0.1:8001/admin")
            
    except Exception as e:
        print(f"❌ Error creating demo data: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()