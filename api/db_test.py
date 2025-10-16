import os
import sys
import json
from pathlib import Path

# Add project to Python path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# Set environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

def test_database_clean():
    """Clean database test without Django conflicts"""
    
    try:
        # Import Django and setup
    import django
    # django.setup()  # Disabled to prevent reentrant initialization
        
        from django.db import connection
        from django.contrib.auth import get_user_model
        from django.contrib.auth.models import Group
        
        User = get_user_model()
        
        # Test database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()[0]
        
        # Get basic stats
        user_count = User.objects.count()
        group_count = Group.objects.count()
        
        # Try to get course info
        course_count = 0
        try:
            from course.models import Course
            course_count = Course.objects.count()
        except:
            pass
        
        return {
            "status": "success",
            "message": "Database connection successful",
            "user_count": user_count,
            "group_count": group_count,
            "course_count": course_count,
            "database_engine": connection.settings_dict.get('ENGINE', 'Unknown'),
            "database_name": connection.settings_dict.get('NAME', 'Unknown')
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "error_type": type(e).__name__
        }

def app(environ, start_response):
    """Simple database test handler"""
    
    # Get path
    path = environ.get('PATH_INFO', '/')
    
    if path == '/db-test/':
        # Database test endpoint
        result = test_database_clean()
        
        status = '200 OK'
        headers = [
            ('Content-Type', 'application/json'),
            ('Access-Control-Allow-Origin', '*'),
        ]
        start_response(status, headers)
        
        return [json.dumps(result, indent=2).encode('utf-8')]
    
    else:
        # Default response
        status = '200 OK'
        headers = [
            ('Content-Type', 'text/html; charset=utf-8'),
            ('Access-Control-Allow-Origin', '*'),
        ]
        start_response(status, headers)
        
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>SavvyIndians LMS - Database Test</title>
            <style>
                body { font-family: Arial, sans-serif; padding: 40px; background: #f5f5f5; }
                .container { max-width: 800px; margin: 0 auto; background: white; padding: 40px; border-radius: 10px; }
                .success { color: #28a745; }
                .btn { 
                    display: inline-block; 
                    background: #007bff; 
                    color: white; 
                    padding: 10px 20px; 
                    text-decoration: none; 
                    border-radius: 5px; 
                    margin: 5px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1 class="success">🎉 SavvyIndians LMS - Database Testing</h1>
                <p>This is a clean Django database test endpoint.</p>
                
                <h3>🔧 Available Endpoints:</h3>
                <ul>
                    <li><a href="/db-test/" class="btn">📊 Database Test</a></li>
                </ul>
                
                <p><strong>✅ Status:</strong> Serverless function is working!</p>
                <p><strong>🔧 Purpose:</strong> Test database connectivity without Django conflicts</p>
            </div>
        </body>
        </html>
        """
        
        return [html.encode('utf-8')]