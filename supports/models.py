from django.db import models

# Create your models here.
class Support(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contribute_fund = models.IntegerField()
    payment_method = models.CharField(max_length=10)
    donated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-donated_date']
        indexes = [models.Index(fields=['donated_date'])]
        
    def __str__(self):
        return self.level