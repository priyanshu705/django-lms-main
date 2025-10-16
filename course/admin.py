from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.html import format_html

from .models import Program, Course, CourseAllocation, Upload, UploadVideo
from modeltranslation.admin import TranslationAdmin

class ProgramAdmin(TranslationAdmin):
    list_display = ['title', 'summary']
    search_fields = ['title', 'summary']

class CourseAdmin(TranslationAdmin):
    list_display = ['title', 'code', 'program', 'level', 'year', 'semester', 'credit']
    list_filter = ['program', 'level', 'year', 'semester', 'is_elective']
    search_fields = ['title', 'code', 'summary']

class UploadAdmin(TranslationAdmin):
    list_display = ['title', 'course', 'upload_time']
    list_filter = ['course', 'upload_time']
    search_fields = ['title', 'course__title']

class UploadVideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'is_youtube_video', 'video_preview', 'timestamp']
    list_filter = ['course', 'is_youtube_video', 'timestamp']
    search_fields = ['title', 'course__title', 'summary']
    readonly_fields = ['slug', 'is_youtube_video', 'video_thumbnail_preview']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'course', 'summary')
        }),
        ('Video Source', {
            'fields': ('youtube_url', 'video'),
            'description': 'Provide either a YouTube URL (recommended for storage optimization) or upload a video file.'
        }),
        ('Auto-Generated Fields', {
            'fields': ('slug', 'is_youtube_video', 'video_duration'),
            'classes': ('collapse',)
        }),
        ('Preview', {
            'fields': ('video_thumbnail_preview',),
            'classes': ('collapse',)
        })
    )

    def video_preview(self, obj):
        """Display video type and preview link"""
        if obj.is_youtube_video and obj.youtube_url:
            video_id = obj.get_youtube_video_id()
            if video_id:
                thumbnail_url = f"https://img.youtube.com/vi/{video_id}/default.jpg"
                return format_html(
                    '<img src="{}" width="60" height="45" style="border-radius: 4px;"> <br><small>📺 YouTube</small>',
                    thumbnail_url
                )
            return "📺 YouTube"
        elif obj.video:
            return "🎬 File Upload"
        return "❌ No Video"
    
    video_preview.short_description = "Video Preview"

    def video_thumbnail_preview(self, obj):
        """Show larger thumbnail preview in admin"""
        if obj.is_youtube_video and obj.youtube_url:
            video_id = obj.get_youtube_video_id()
            if video_id:
                thumbnail_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
                youtube_link = obj.youtube_url
                return format_html(
                    '<div style="text-align: center;">'
                    '<img src="{}" style="max-width: 300px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"><br>'
                    '<small><a href="{}" target="_blank">🔗 View on YouTube</a></small>'
                    '</div>',
                    thumbnail_url, youtube_link
                )
        return "No preview available"
    
    video_thumbnail_preview.short_description = "Thumbnail Preview"

admin.site.register(Program, ProgramAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseAllocation)
admin.site.register(Upload, UploadAdmin)
admin.site.register(UploadVideo, UploadVideoAdmin)
