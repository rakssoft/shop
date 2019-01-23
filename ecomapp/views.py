from django.shortcuts import render
from django.http import HttpResponseRedirect
from ecomapp.models import Category, Product, CartItem, Cart, Images


# Create your views here.

def base_view(request):
    cart = Cart.objects.first()
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categorise': categories,
        'products': products,
        'cart': cart
    }
    return render(request, 'base.html', context)


def product_view(request, product_slug):
    cart = Cart.objects.first()
    product = Product.objects.get(slug=product_slug)
    categories = Category.objects.all()
    context = {
        'product': product,
        'categorise': categories,
        'cart': cart
    }
    return render(request, 'product.html', context)


def category_view(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    product_of_category = Product.objects.filter(category=category)
    categories = Category.objects.all()
    context = {
        #   'category': category,
        'product_of_category': product_of_category,
        'categorise': categories,
    }
    return render(request, 'category.html', context)


def cart_view(request):
    cart = Cart.objects.first()
    context = {
        'cart': cart
    }
    return render(request, 'cart.html', context)


def add_to_cart_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    new_item, _ = CartItem.objects.get_or_create(product=product, item_tottal=product.price)
    cart = Cart.objects.first()
    if new_item not in cart.item.all():
        cart.item.add(new_item)
        cart.save()
        return HttpResponseRedirect('/cart/')


def o_nas(request):
    cart = Cart.objects.first()
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categorise': categories,
        'products': products,
        'cart': cart
    }
    return render(request, 'o_nas.html', context)


def contact(request):
    cart = Cart.objects.first()
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categorise': categories,
        'products': products,
        'cart': cart
    }
    return render(request, 'contact.html', context)


def online_diagnos(request):
    cart = Cart.objects.first()
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categorise': categories,
        'products': products,
        'cart': cart
    }
    return render(request, 'online_diagnos.html', context)


def images(request):
    image = Images.objects.get()
    cart = Cart.objects.first()
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'image': image,
        'categorise': categories,
        'products': products,
        'cart': cart
    }

    return render(request, 'contact.html', context)


def base2(request):
    cart = Cart.objects.first()
    product = Product.objects.get()
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categorise': categories,
        'products': products,
        'cart': cart,
        'product': product,
    }
    return render(request, 'base2.html', context)


