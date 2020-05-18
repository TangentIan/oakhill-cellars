from datetime import datetime

from django.db import models


class Catalog(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Product(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to="product_photo", blank=True)
    producer = models.CharField(max_length=300, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
