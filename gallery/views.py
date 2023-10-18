from django.shortcuts import render
from .models import Image

def van_images(request):
    images = Image.objects.all()
    
    return render(
            request,
            "van_images.html",
            {'images': images}
        )
