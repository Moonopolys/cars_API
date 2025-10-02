from rest_framework import serializers
from django.core.validators import MinValueValidator
from .models import Car, Owner, Brand

class CarSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    brand = serializers.SlugRelatedField(
        slug_field="name",
        queryset=Brand.objects.all()
    )
    year = serializers.IntegerField()
    color = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

class OwnerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    phone = serializers.CharField(max_length=20)
    car_id = serializers.IntegerField()

    def create(self, validated_data):
        return Owner.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class BrandSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Brand.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance