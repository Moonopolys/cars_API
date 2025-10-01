from rest_framework import serializers
from django.core.validators import MinValueValidator
from .models import Car, Owner

class CarSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    brand = serializers.CharField(max_length=255)
    year = serializers.IntegerField()
    color = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

class OwnerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    phone = serializers.CharField(max_length=20)
    car_id = serializers.IntegerField()

    def create(self, validated_data):
        return Owner.objects.create(**validated_data)