from django.contrib import admin
from django.db import models

# Create your models here.

class Tutor(models.Model):
    tutor_name = models.CharField(max_length=50)
    detail = models.CharField(max_length=50)
    experience = models.CharField(max_length=500)
    tutor_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    

    def __str__(self):
        return self.tutor_name 
