from django.contrib import admin
from django.urls import path

from product import views
app_name = 'product'

urlpatterns = [
    path('products/', views.products, name='products'),
]
