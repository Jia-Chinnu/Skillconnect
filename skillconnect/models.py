from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    skills = models.CharField(max_length=255)  # Store skills as a comma-separated string

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    required_skills = models.CharField(max_length=255)  # Skills required for the job
    posted_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
