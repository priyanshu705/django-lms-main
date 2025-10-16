#!/usr/bin/env python
"""
Test Django initialization locally
"""
import os
import sys
from pathlib import Path

# Add project to Python path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

try:
    import django
    print(f"Django version: {django.get_version()}")
    
    # Setup Django
    django.setup()
    print("Django setup successful")
    
    # Test database
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        print(f"Database test successful: {result}")
    
    # Test URL patterns
    from django.urls import get_resolver
    resolver = get_resolver()
    print(f"URL patterns loaded: {len(resolver.url_patterns)}")
    
    # Test WSGI app
    from django.core.wsgi import get_wsgi_application
    app = get_wsgi_application()
    print(f"WSGI application created: {type(app)}")
    
    print("All tests passed!")
    
except Exception as e:
    import traceback
    print(f"Error: {e}")
    print("Full traceback:")
    traceback.print_exc()