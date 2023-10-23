from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.TextField(blank=True, max_length=500)
    image = models.ImageField(upload_to='media/')
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name="image_author")
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title
