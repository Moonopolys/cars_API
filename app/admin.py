from django.contrib import admin
from .models import Car, Owner, Brand, Color

admin.site.register(Brand)
admin.site.register(Car)
admin.site.register(Color)
admin.site.register(Owner)
