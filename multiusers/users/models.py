from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    phone=models.IntegerField(blank=True, null=True)
    role=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)