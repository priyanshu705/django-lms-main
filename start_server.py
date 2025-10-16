import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
# django.setup()  # Disabled to prevent reentrant initialization
from django.core.management import execute_from_command_line
execute_from_command_line(['start_server.py', 'runserver'])