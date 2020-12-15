from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('products', views.all, name="all"),
    path('products/<slug:slug>', views.single, name="single"),
]
