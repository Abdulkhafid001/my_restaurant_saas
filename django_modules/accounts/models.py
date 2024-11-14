from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class NaijaKitchenUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=20)
