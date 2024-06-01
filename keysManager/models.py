from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    # Add other fields as needed

class AccessKey(models.Model):
    key = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20)
    date_procured = models.DateField()
    expiry_date = models.DateField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    # Add other fields as needed

class User(AbstractUser):
    # Add custom fields if necessary
    pass