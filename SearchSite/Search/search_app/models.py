from django.db import models
from django.contrib.postgres.search import SearchVectorField, SearchVector

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    search = SearchVectorField(null=True)

    def __str__(self):
        return self.name
Car.objects.all().update(search=SearchVector('name'))
