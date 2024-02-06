from django.urls import path
from . import views
from .views import NewPhoto
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('van_images/', views.van_images, name='van_images'),
    path('new_photo/', login_required (NewPhoto.as_view()), name='new_photo'),
]
