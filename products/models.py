from django.db import models


class Product(models.Model):
    title = models.CharField(max_length = 120, null = False, blank = False)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    sale_price = models.DecimalField(decimal_places=2, max_digits=10, default = 0)
    slug = models.SlugField(unique = True)
    timestamp = models.DateTimeField(auto_now_add= True, auto_now=False)
    quantity = models.IntegerField(default=1)
    updated = models.DateTimeField(auto_now_add= False, auto_now=True)
    active = models.BooleanField(default= True)

    class Meta:
        unique_together = ('title', 'slug')
    
    def __str__(self):
        return self.title

    def get_price(self):
        return self.price

# Create your models here.
