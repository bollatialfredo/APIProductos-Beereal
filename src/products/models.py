from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.IntegerField()
    price = models.IntegerField()
    stock = models.IntegerField()
    condition = models.CharField(max_length=255)
# Create your models here.
