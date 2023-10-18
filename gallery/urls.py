from django.urls import path
from . import views

urlpatterns = [
    path('van_images', views.van_images, name='van_images'),
]