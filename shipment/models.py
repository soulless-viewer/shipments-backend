from django.db import models


class Shipment(models.Model):
    departure_dt = models.DateTimeField()
    arrival_dt = models.DateTimeField()
    departure_point = models.CharField(max_length=255)
    arrival_point = models.CharField(max_length=255)
    cargo_volume = models.IntegerField(default=100)

    class Meta:
        ordering = ["departure_dt"]
