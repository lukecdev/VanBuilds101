from django.urls import path
from . import views
from .views import NewPhoto

urlpatterns = [
    path('van_images/', views.van_images, name='van_images'),
    path('new_photo/', NewPhoto.as_view(), name='new_photo'),
]
