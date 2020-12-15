from django.shortcuts import render
from .models import Product
from carts.models import Cart
from accounts.models import Profile

def all(request):
    products = Product.objects.all()
    cart = Cart.objects.all()[0]
    profile = Profile.objects.all();
    context = {'products' : products, "cart" : cart, "profile" : profile}
    template = 'Cart.html'
    return render(request, template, context)

def single(request, slug):
    product = Product.objects.get(slug = slug)
    cart = Cart.objects.all()[0]
    context = {'product' : product, "cart" : cart}
    template = 'single.html'
    return render(request, template, context)
# Create your views here.
