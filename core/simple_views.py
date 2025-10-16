from django.http import HttpResponse
from django.shortcuts import render

def simple_home_view(request):
    """Simplified homepage without database dependencies"""
    
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SavvyIndians Learning Management System</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                color: white;
            }
            .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
            .header { text-align: center; padding: 60px 0; }
            .logo { font-size: 3.5rem; font-weight: bold; margin-bottom: 20px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
            .tagline { font-size: 1.3rem; opacity: 0.9; margin-bottom: 40px; }
            .hero { background: rgba(255,255,255,0.1); padding: 40px; border-radius: 20px; margin: 40px 0; backdrop-filter: blur(10px); }
            .features { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin: 40px 0; }
            .feature { background: rgba(255,255,255,0.1); padding: 30px; border-radius: 15px; text-align: center; }
            .feature h3 { font-size: 1.5rem; margin-bottom: 15px; color: #4CAF50; }
            .auth-buttons { text-align: center; margin: 40px 0; }
            .btn { 
                display: inline-block; padding: 15px 30px; margin: 10px; 
                background: rgba(76, 175, 80, 0.8); color: white; text-decoration: none; 
                border-radius: 25px; font-weight: bold; transition: all 0.3s;
            }
            .btn:hover { background: rgba(76, 175, 80, 1); transform: translateY(-2px); }
            .btn-google { background: rgba(219, 68, 55, 0.8); }
            .btn-google:hover { background: rgba(219, 68, 55, 1); }
            .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 40px 0; }
            .stat { text-align: center; background: rgba(255,255,255,0.1); padding: 20px; border-radius: 10px; }
            .stat-number { font-size: 2rem; font-weight: bold; color: #4CAF50; }
            @media (max-width: 768px) {
                .logo { font-size: 2.5rem; }
                .features { grid-template-columns: 1fr; }
                .container { padding: 10px; }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="logo">🎓 SavvyIndians LMS</div>
                <p class="tagline">Learn Smart, Grow Fast - Your Gateway to Knowledge</p>
            </div>
            
            <div class="hero">
                <h2 style="text-align: center; margin-bottom: 20px;">Welcome to SavvyIndians Learning Management System</h2>
                <p style="text-align: center; font-size: 1.1rem; opacity: 0.9;">
                    Empowering students with cutting-edge online education. Join thousands of learners 
                    on their journey to success with our comprehensive course platform.
                </p>
            </div>
            
            <div class="auth-buttons">
                <a href="/accounts/student/register/" class="btn">📝 Register Now</a>
                <a href="/accounts/student/login/" class="btn">🔐 Student Login</a>
                <a href="/auth/google/login/" class="btn btn-google">🔑 Login with Google</a>
                <a href="/admin/" class="btn" style="background: rgba(255, 152, 0, 0.8);">⚙️ Admin Panel</a>
            </div>
            
            <div class="stats">
                <div class="stat">
                    <div class="stat-number">500+</div>
                    <div>Courses Available</div>
                </div>
                <div class="stat">
                    <div class="stat-number">10K+</div>
                    <div>Active Students</div>
                </div>
                <div class="stat">
                    <div class="stat-number">100+</div>
                    <div>Expert Instructors</div>
                </div>
                <div class="stat">
                    <div class="stat-number">24/7</div>
                    <div>Learning Support</div>
                </div>
            </div>
            
            <div class="features">
                <div class="feature">
                    <h3>🎥 HD Video Lectures</h3>
                    <p>High-quality video content with crystal clear audio and visual presentation for the best learning experience.</p>
                </div>
                <div class="feature">
                    <h3>📚 Comprehensive Courses</h3>
                    <p>Wide range of subjects from technology to business, designed by industry experts and academic professionals.</p>
                </div>
                <div class="feature">
                    <h3>🏆 Certification</h3>
                    <p>Earn recognized certificates upon course completion to boost your career and validate your skills.</p>
                </div>
                <div class="feature">
                    <h3>📱 Mobile Learning</h3>
                    <p>Learn on-the-go with our mobile-optimized platform. Access courses anytime, anywhere, on any device.</p>
                </div>
                <div class="feature">
                    <h3>🤝 Community Support</h3>
                    <p>Join study groups, participate in discussions, and get help from peers and instructors.</p>
                </div>
                <div class="feature">
                    <h3>📊 Progress Tracking</h3>
                    <p>Monitor your learning progress with detailed analytics and personalized recommendations.</p>
                </div>
            </div>
            
            <div style="text-align: center; padding: 40px 0; opacity: 0.8;">
                <p>&copy; 2025 SavvyIndians LMS. Empowering Education, Enabling Success.</p>
                <p style="margin-top: 10px;">🌐 Deployed on Vercel | 🗄️ PostgreSQL Database | 🔐 Google OAuth Ready</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return HttpResponse(html_content)