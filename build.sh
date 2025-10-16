#!/bin/bash
# SavvyIndians LMS - Vercel Build Script

echo "🚀 Starting SavvyIndians LMS Build Process..."

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Set environment variables
export DJANGO_SETTINGS_MODULE=config.settings
export DEBUG=False

# Create necessary directories
echo "📁 Creating required directories..."
mkdir -p staticfiles
mkdir -p media/uploads
mkdir -p media/registration_form
mkdir -p media/result_sheet

# Collect static files
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput --clear

# Run migrations
echo "🗄️ Running database migrations..."
python manage.py migrate --noinput

# Create superuser if it doesn't exist
echo "👤 Setting up admin user..."
python manage.py shell << EOF
from accounts.models import User
if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@savvyindians.com', 
        password='admin123',
        first_name='Admin',
        last_name='User'
    )
    print('✅ Superuser created successfully!')
else:
    print('✅ Superuser already exists!')
EOF

# Create demo data if needed
echo "🎯 Setting up demo data..."
python scripts/create_demo_data.py --skip-existing

echo "✅ Build completed successfully!"
echo "🎉 SavvyIndians LMS is ready for deployment!"