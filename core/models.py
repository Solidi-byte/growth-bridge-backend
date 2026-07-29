from django.db import models
from django.contrib.auth.models import User

class University(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    country = models.CharField(max_length=100, db_index=True)
    city = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    portal_url = models.URLField(blank=True, null=True)
    logo_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = "Universities"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.country})"


class Program(models.Model):
    DEGREE_CHOICES = [
        ('bachelor', "Bachelor's"),
        ('master', "Master's"),
        ('phd', 'PhD'),
        ('diploma', 'Diploma'),
    ]

    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='programs')
    title = models.CharField(max_length=255, db_index=True)
    field_of_study = models.CharField(max_length=150, db_index=True)
    degree_level = models.CharField(max_length=20, choices=DEGREE_CHOICES, db_index=True)
    tuition_fee_annual = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, db_index=True)
    currency = models.CharField(max_length=10, default='EUR')
    duration_years = models.DecimalField(max_digits=3, decimal_places=1, default=1.0)
    language_requirements = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title} - {self.university.name}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    target_country = models.CharField(max_length=100, blank=True, null=True)
    quiz_score = models.IntegerField(default=0)
    quiz_completed = models.BooleanField(default=False)
    saved_programs = models.ManyToManyField(Program, blank=True, related_name='saved_by_users')

    def __str__(self):
        return f"Profile of {self.user.username}"


class JobListing(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    company = models.CharField(max_length=150)
    location = models.CharField(max_length=100, default="Remote")
    salary = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} at {self.company}"