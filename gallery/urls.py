from django.urls import path
from . import views
from .views import NewPhoto, UpdateGalleryView, DeleteGalleryView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('van_images/', views.van_images, name='van_images'),
    path('new_photo/', login_required (NewPhoto.as_view()), name='new_photo'),
    path('update_gallery/<slug:slug>', login_required (UpdateGalleryView.as_view()), name='update_gallery'),
    path('delete_gallery/<slug:slug>/delete', login_required (DeleteGalleryView.as_view()), name='delete_gallery'),


]
