from django.contrib import admin

# Register your models here.
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ("name", "brand",)

admin.site.register(Car, CarAdmin)