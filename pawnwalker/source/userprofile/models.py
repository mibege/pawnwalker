from django.db import models

# Create your models here.
from accounts.models import Activation
from django.contrib.auth.models import User
from django.conf import settings


class userProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=120, null=False, blank=False)
    city = models.CharField(max_length=120, null=False, blank=False)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    isDogwalker = models.BooleanField(default=True)
