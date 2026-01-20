from tutors.models import Tutor
from django.contrib import admin
from django.db import models

# Create your models here.

class Workshop(models.Model):
    workshop = models.CharField(max_length=50)
    ws_type = models.CharField(max_length=20)
    # age_group = models.CharField(max_length=10)
    # course_Location = models.CharField(max_length=10)
    day_of_the_week = models.CharField(max_length=3)
    start_date = models.DateField()
    start_time = models.TimeField()
    fee = models.IntegerField()
    ws_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    tagline = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    enrolment_no = models.IntegerField()
    applied_no = models.IntegerField()
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(auto_now_add=True)
    tutor = models.ForeignKey(Tutor, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['-start_date', '-start_time']
        indexes = [models.Index(fields=['start_date'])]
        
    def __str__(self):
        return self.workshop
