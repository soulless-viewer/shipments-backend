from rest_framework import serializers
from shipment.models import Shipment


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = [
            "id",
            "arrival_dt",
            "departure_dt",
            "cargo_volume",
            "arrival_point",
            "departure_point"
        ]
