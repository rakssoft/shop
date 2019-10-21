from django.urls import include, path, re_path
from ecomapp.views import base_view, category_view, product_view, cart_view, add_to_cart_view, base2, o_nas, contact, online_diagnos, images
from django.contrib import admin
from django.urls import path
from ecomapp.views import *




urlpatterns = [
    re_path(r'^category/(?P<category_slug>[-\w]+)/$', category_view, name='category_detail'),
    re_path(r'^product/(?P<product_slug>[-\w]+)/$', product_view, name='product_detail'),
    re_path(r'^add_to_cart/(?P<product_slug>[-\w]+)/$', add_to_cart_view, name='add_to_cart'),
    re_path(r'^cart/$', cart_view, name = 'cart'),
    re_path(r'$^', base_view, name='base'),
    path('base2/', base2, name='base2'),
    path('o_nas/', o_nas, name='o_nas'),


    path('contact/', contact, name='contact'),

    path('online_diagnos/', online_diagnos, name='online_diagnos'),

    path('email/', emailView, name='email'),

# sendemail/urls.py



]
