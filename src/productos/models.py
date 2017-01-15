from __future__ import unicode_literals

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()
# Create your models here.
