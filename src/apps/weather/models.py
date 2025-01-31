from django.db import models
from django.db.models import UniqueConstraint

from apps.user.models import CustomUser


class Location(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='locations')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['user', 'latitude', 'longitude'],
                name='unique_user_coordinate'
            )
        ]
