from django.contrib import admin
from django.db import models
from django.utils import timezone

# Create your models here.

class Workshop(models.Model):
    workshop = models.CharField(max_length=50, default=' ')
    ws_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # ws_type = models.CharField(max_length=20)
    # age_group = models.CharField(max_length=10)
    # course_Location = models.CharField(max_length=10)
    tutor_name = models.CharField(max_length=50, default=' ')
    tagline = models.CharField(max_length=50, default=' ')
    experience = models.CharField(max_length=500, default=' ')
    tutor_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    quote = models.CharField(max_length=50, default=' ')
    detail = models.CharField(max_length=500, default=' ')

    day_of_the_week = models.CharField(max_length=3, default=' ')
    start_date = models.DateField()
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)
    # fee = models.IntegerField()
    # tagline = models.CharField(max_length=100)
    # description = models.CharField(max_length=500)
    enrolment_no = models.IntegerField()
    applied_no = models.IntegerField()
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(auto_now_add=True)
    level = models.IntegerField()


    class Meta:
        ordering = ['-start_date', '-start_time']
        indexes = [models.Index(fields=['start_date'])]
        
    def __str__(self):
        return self.workshop
