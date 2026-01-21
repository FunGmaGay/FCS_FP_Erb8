from workshops.models import Workshop
from django.conf import settings
from django.db import models

class Enrolment(models.Model):
    auth_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    age_range = models.CharField(max_length=10)
    zone = models.CharField(max_length=10)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    applied_date = models.DateTimeField()
    workshop = models.ForeignKey(Workshop, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.last_name

# Create your models here.
