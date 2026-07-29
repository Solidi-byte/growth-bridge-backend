from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UniversityViewSet, ProgramViewSet, UserProfileViewSet, JobListingViewSet

router = DefaultRouter()
router.register(r'universities', UniversityViewSet, basename='university')
router.register(r'programs', ProgramViewSet, basename='program')
router.register(r'profiles', UserProfileViewSet, basename='userprofile')
router.register(r'jobs', JobListingViewSet, basename='joblisting')

urlpatterns = [
    path('', include(router.urls)),
]
