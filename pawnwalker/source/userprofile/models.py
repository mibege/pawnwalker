from django.db import models

# Create your models here.
from accounts.models import Activation
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class userProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=130, null=False, blank=False)
    address = models.CharField(max_length=120, null=False, blank=False)
    city = models.CharField(max_length=120, null=False, blank=False)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    isDogwalker = models.BooleanField(default=True)
