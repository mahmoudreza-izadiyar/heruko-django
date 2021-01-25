from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Preset(models.Model):
    locationName = models.CharField(max_length=100)
    latitude = models.FloatField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)],
        null=False
    )
    longitude = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)],
        null=False
    )
    objects = models.Manager()


class FavouritePlaces(models.Model):
    url = models.URLField(max_length=200, blank=False, default='')
    latitude = models.FloatField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)],
    )
    longitude = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)],
    )
    objects = models.Manager()


