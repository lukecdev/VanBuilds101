from django.shortcuts import render, redirect
from .models import Image
from django.views import generic
from django.urls import reverse_lazy
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
    fields = ['title', 'slug', 'excerpt', 'gallery_image']

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)


class UpdateGalleryView(generic.UpdateView):
    model = Image
    template_name = "update_gallery.html"
    fields = ['title','slug', 'gallery_image', 'excerpt']

class DeleteGalleryView(generic.DeleteView):
    model = Image
    template_name = "delete_gallery.html"
    success_url = reverse_lazy('van_images')
    fields = ['title','slug', 'gallery_image', 'excerpt']  
