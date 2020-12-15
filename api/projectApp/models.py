from django.db import models

class Store(models.Model):
    brand = models.IntegerField()
    identifier = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    thumbnail = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.identifier