from django.shortcuts import render,redirect
from .models import Cart
from accounts.models import Profile
from django.contrib.auth.models import User
from products.models import Product

def view_cart(request):
    cart = Cart.objects.all()[0]
    context = {"cart" : cart}
    template = "cart.html"
    return render(request, template, context)


def update_cart(request, slug):
    cart = Cart.objects.all()[0]
    product = Product.objects.get(slug = slug)
    if not product in cart.products.all():
        cart.products.add(product)
        product.quantity = 1
        product.save()
    else:
        cart.products.remove(product)
    new_total = 0.00
    for item in cart.products.all():
        new_total += float(item.price)*float(item.quantity)
    cart.total = new_total
    cart.save()
    return redirect("/products")

def up_quantity(request, slug):
    product = Product.objects.get(slug = slug)
    cart = Cart.objects.all()[0]
    if product.quantity < 5:
        product.quantity += 1
        cart.total += product.price
        cart.save()
    product.save()
    return redirect("/products")

def down_quantity(request, slug):
    product = Product.objects.get(slug = slug)
    cart = Cart.objects.all()[0]
    if product.quantity != 1:
        product.quantity -= 1
        cart.total -= product.price
        cart.save()
    product.save()
    return redirect("/products")