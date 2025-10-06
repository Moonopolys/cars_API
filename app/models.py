from django.db import models
from django.core.validators import MinValueValidator


class Color(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="brand")
    year = models.IntegerField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name


class Owner(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=100)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='owners')

    def __str__(self):
        return self.name