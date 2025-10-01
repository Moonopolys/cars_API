from django.contrib import admin
from .models import Car, Owner, Brand

admin.site.register(Brand)
admin.site.register(Car)
admin.site.register(Owner)
