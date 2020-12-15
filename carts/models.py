from django.db import models
from products.models import Product


class Cart(models.Model):
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return "Cart Id : %s" % self.pk

    def all_items(self):
        for item in self.products:
            return item.title

# Create your models here.
