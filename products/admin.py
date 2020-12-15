from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active', 'updated']
    readonly_fields = ['timestamp', 'updated']
    prepopulated_fields = {"slug" : ("title", ) }
    class Meta:
        model = Product



admin.site.register(Product, ProductAdmin)
# Register your models here.
