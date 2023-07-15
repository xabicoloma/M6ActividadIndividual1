from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.bienvenida, name='blog-home'),
    path('contacto/', views.contacto, name='contacto-home')
]