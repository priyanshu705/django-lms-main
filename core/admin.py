from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Session, Semester, NewsAndEvents

# Temporarily using standard ModelAdmin instead of TranslationAdmin
class NewsAndEventsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Semester)
admin.site.register(Session)
admin.site.register(NewsAndEvents, NewsAndEventsAdmin)
