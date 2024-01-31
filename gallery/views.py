from django.shortcuts import render, redirect
from .models import Image
from django.views import generic
from django.contrib.auth.decorators import login_required


def van_images(request):
        images = Image.objects.all()
    
        return render(
            request,
            "van_images.html",
            {'images': images}
        )

       
class NewPhoto(generic.CreateView):
    model = Image
    template_name = "new_photo.html"
    fields = ['title', 'slug', 'excerpt', 'image', 'author', 'approved']

