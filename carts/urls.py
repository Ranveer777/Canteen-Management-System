
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name = "view_cart"),
    path('<slug:slug>', views.update_cart, name = "update_cart"),
    path('up_quantity/<slug:slug>', views.up_quantity, name = "up_quantity"),
    path('down_quantity/<slug:slug>', views.down_quantity, name = "down_quantity"),
]
