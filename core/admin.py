from django.contrib import admin
from .models import University, Program, UserProfile, JobListing

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'created_at')
    search_fields = ('name', 'country', 'city')

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'university', 'degree_level', 'tuition_fee_annual', 'is_active')
    list_filter = ('degree_level', 'is_active', 'university__country')
    search_fields = ('title', 'field_of_study', 'university__name')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz_score', 'quiz_completed', 'target_country')

@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'salary', 'created_at')
    search_fields = ('title', 'company', 'location')