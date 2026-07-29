from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import University, Program, UserProfile, JobListing
from .serializers import (
    UniversitySerializer, 
    ProgramSerializer, 
    UserProfileSerializer, 
    JobListingSerializer
)

class UniversityViewSet(viewsets.ModelViewSet):
    """
    Handles the Explore page for Universities. 
    This pulls ALL universities added in the admin panel.
    """
    queryset = University.objects.all().order_by('name')
    serializer_class = UniversitySerializer

    def get_queryset(self):
        # This allows you to safely filter by country in Next.js 
        # (e.g., /api/universities/?country=Germany) without breaking the main explore page.
        queryset = super().get_queryset()
        country = self.request.query_params.get('country', None)
        
        if country:
            queryset = queryset.filter(country__iexact=country)
            
        return queryset


class ProgramViewSet(viewsets.ModelViewSet):
    """
    Handles academic programs linked to universities.
    Only returns programs marked as active in the admin.
    """
    queryset = Program.objects.filter(is_active=True).order_by('title')
    serializer_class = ProgramSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # Optional: Filter programs by degree level
        degree = self.request.query_params.get('degree_level', None)
        if degree:
            queryset = queryset.filter(degree_level__iexact=degree)
        return queryset


class JobListingViewSet(viewsets.ModelViewSet):
    """
    Handles the Explore page for Jobs.
    Pulls all jobs sorted by the newest first.
    """
    queryset = JobListing.objects.all().order_by('-created_at')
    serializer_class = JobListingSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    Handles the user profiles and quiz scores.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer