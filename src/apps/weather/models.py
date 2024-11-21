from django.db import models
from django.db.models import IntegerField, CharField, DecimalField

from apps.user.models import CustomUser


class Location(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='locations')
    Latitude = models.DecimalField(max_digits=9, decimal_places=6)
    Longitude = models.DecimalField(max_digits=9, decimal_places=6)