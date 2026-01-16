from django.contrib import admin
from django.db import models

# Create your models here.

class Workshops(models.Model):
    title = models.CharField(max_length=50)
   # level = models.IntegerField()
   # age_group = models.CharField(max_length=10)
   # course_Location = models.CharField(max_length=10)
    day_of_the_week = models.CharField(max_length=3)
    session_no = models.IntegerField()
    start_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    fee = models.IntegerField()
    tagline = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    enrolment_no = models.IntegerField()
    applied_no = models.IntegerField()
    tutor_name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    experience = models.CharField(max_length=500)
    ws_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    tutor_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_date', '-start_time']
        indexes = [models.Index(fields=['start_date'])]
        
    def __str__(self):
        return self.level


