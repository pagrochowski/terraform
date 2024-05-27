from django.contrib import admin
from django.db.models import Count
from .models import *


@admin.register(Macro_Project)
class MacroProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_file', 'created_at', 'order')
    fields = ('title', 'description', 'video_file', 'screenshot', 'disclaimer', 'code_snippet', 'order')  # Order of fields in form
    search_fields = ('title', 'description')  # Add search
    list_filter = ('created_at',)            # Add filtering

@admin.register(Script_Project)
class ScriptProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_file', 'created_at', 'order')
    fields = ('title', 'description', 'video_file', 'screenshot', 'disclaimer','code_snippet', 'order')  # Order of fields in form
    search_fields = ('title', 'description')  # Add search
    list_filter = ('created_at',)            # Add filtering


@admin.register(Website_Project)
class WebsiteProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_file', 'created_at', 'order')
    fields = ('title', 'description', 'link', 'video_file', 'screenshot', 'disclaimer', 'order')  # Order of fields in form
    search_fields = ('title', 'description')  # Add search
    list_filter = ('created_at',)            # Add filtering


@admin.register(Education_Project)
class EducationProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_file', 'created_at', 'order')
    fields = ('title', 'description', 'link', 'certificate', 'video_file', 'screenshot', 'disclaimer', 'order')  # Order of fields in form
    search_fields = ('title', 'description')  # Add search
    list_filter = ('created_at',)            # Add filtering


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    pass  # You can customize this further if needed


@admin.register(SessionVisit)
class SessionVisitAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'visit_count', 'visit_time', 'last_activity')
    readonly_fields = ('session_key', 'visit_count', 'visit_time', 'last_activity')
    ordering = ('-visit_count',)  # Order by visit count (descending)
    list_filter = ('visit_time',)  # Add this line

