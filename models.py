from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.urls.base import reverse

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.city} ( {self.code})"

class Flights(models.Model):
    origin = models.ForeignKey(Airport, on_delete=CASCADE, related_name="departure")
    destination = models.ForeignKey(Airport, on_delete=CASCADE, related_name="arrival")
    duration = models.IntegerField()
    def __str__(self):
        return f"{self.origin} -> {self.destination} IN {self.duration}"