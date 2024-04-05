from django.contrib import admin
from .models import JobPost, JobApplication

# Register your models here.
# admin.site.register(JobPost)
# admin.site.register(JobApplication)

class JobApplicationInline(admin.TabularInline):
    model = JobApplication

@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    inlines = [JobApplicationInline]

admin.site.register(JobApplication)