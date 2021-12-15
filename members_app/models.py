from django.db import models


# Create your models here.
class Members(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(max_length=255)
    birth = models.DateField(max_length=255)
    email = models.EmailField(max_length=255, blank=True)
