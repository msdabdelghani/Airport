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

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=CASCADE, related_name="departure")
    destination = models.ForeignKey(Airport, on_delete=CASCADE, related_name="arrival")
    duration = models.IntegerField()
    def __str__(self):
        return f"{self.origin} -> {self.destination} IN {self.duration}"

class Passenger(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    flights = models.ManyToManyField(Flight, blank= True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"