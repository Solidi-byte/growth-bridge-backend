from rest_framework import serializers
from django.contrib.auth.models import User
from .models import University, Program, UserProfile, JobListing

class UniversitySerializer(serializers.ModelSerializer):
    programs_count = serializers.IntegerField(source='programs.count', read_only=True)

    class Meta:
        model = University
        fields = ['id', 'name', 'country', 'city', 'website', 'description', 'programs_count']


class ProgramSerializer(serializers.ModelSerializer):
    university_details = UniversitySerializer(source='university', read_only=True)

    class Meta:
        model = Program
        fields = [
            'id', 'university', 'university_details', 'title', 'field_of_study',
            'degree_level', 'tuition_fee_annual', 'currency', 'duration_years',
            'language_requirements', 'description', 'is_active'
        ]


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    saved_programs_details = ProgramSerializer(source='saved_programs', many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            'id', 'username', 'email', 'bio', 'target_country',
            'quiz_score', 'quiz_completed', 'saved_programs', 'saved_programs_details'
        ]


class JobListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobListing
        fields = ['id', 'title', 'company', 'location', 'salary', 'description', 'url', 'created_at']
 