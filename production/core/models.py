from django.db import models


# Create your models here.
class Macro_Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    code_snippet = models.TextField()
    video_file = models.FileField(upload_to='project_videos/', null=True, blank=True)
    screenshot = models.FileField(upload_to='project_screenshots/', null=True, blank=True)
    disclaimer = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0)  # PositiveIntegerField for ordering

    class Meta:
        ordering = ['order']  # Order by the 'order' field by default

    def __str__(self):
        return self.title
    
class Script_Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    code_snippet = models.TextField()
    video_file = models.FileField(upload_to='project_videos/', null=True, blank=True)
    screenshot = models.FileField(upload_to='project_screenshots/', null=True, blank=True)
    disclaimer = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0)  # PositiveIntegerField for ordering

    class Meta:
        ordering = ['order']  # Order by the 'order' field by default

    def __str__(self):
        return self.title
    
class Website_Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.TextField()
    video_file = models.FileField(upload_to='project_videos/', null=True, blank=True)
    screenshot = models.FileField(upload_to='project_screenshots/', null=True, blank=True)
    disclaimer = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0)  # PositiveIntegerField for ordering

    class Meta:
        ordering = ['order']  # Order by the 'order' field by default

    def __str__(self):
        return self.title
    

class Education_Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.TextField(null=True, blank=True)
    certificate = models.TextField(null=True, blank=True)
    video_file = models.FileField(upload_to='project_videos/', null=True, blank=True)
    screenshot = models.FileField(upload_to='project_screenshots/', null=True, blank=True)
    disclaimer = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0)  # PositiveIntegerField for ordering

    class Meta:
        ordering = ['order']  # Order by the 'order' field by default

    def __str__(self):
        return self.title
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
    

class SiteConfiguration(models.Model):
    contact_email = models.EmailField()

    def __str__(self):
        return "Site Configuration"


class SessionVisit(models.Model):
    session_key = models.CharField(max_length=40, unique=True)
    visit_count = models.PositiveIntegerField(default=0)
    last_activity = models.DateTimeField(null=True, blank=True)
    visit_time = models.DateTimeField(auto_now_add=True)  # Add this field