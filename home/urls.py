from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('accordion/', views.accordion, name='accordion'),
    path('', views.index, name='about'),
]
