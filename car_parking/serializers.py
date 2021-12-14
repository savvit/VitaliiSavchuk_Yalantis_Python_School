from rest_framework import serializers, fields
from YalantisTest import settings
from car_parking.models import Driver, Vehicle


class DriverListSerializer(serializers.ModelSerializer):
    created_at = fields.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)

    class Meta:
        model = Driver
        fields = '__all__'


class VehicleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
