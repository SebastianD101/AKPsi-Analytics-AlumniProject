from django.db import models

class Alumni(models.Model):
    name = models.CharField(max_length=255)
    linkedin = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    graduation_date = models.IntegerField()
    majors = models.CharField(max_length=255)
    sphere = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    current_company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    previous_companies = models.TextField(blank=True)