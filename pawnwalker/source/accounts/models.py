from django.db import models
from django.contrib.auth.models import User

from django.conf import settings


class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=20, default='kajaanintie 46')
    isDogwalker = models.BooleanField(default=True)


class Event(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    start_month = models.DateField()
    end_month = models.DateField()
    start_year = models.DateField()
    end_year = models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/dogwalker/book/' + str(self.pk)
