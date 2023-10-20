from django.db import models


# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title

class ImageSubmission(models.Model):
    image = models.ImageField(upload_to='media/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
