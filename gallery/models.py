from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Image(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True, default='image')
    excerpt = models.TextField(blank=True, max_length=500)
    gallery_image = CloudinaryField('image', blank=False, default='placeholder')
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name="image_author")
    approved = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('gallery')  

    def __str__(self):
        return self.title
