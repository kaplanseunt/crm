from django.db import models

class Country(models.Model):
    sortname = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=150)
    phonecode = models.IntegerField()

    def __str__(self):
        return self.name
