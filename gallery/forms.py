from .models import Image, ImageSubmission
from django import forms

class Image(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['title', 'excerpt', 'image', 'author', 'approved']

class ImageSubmissionForm(forms.ModelForm):
    class Meta:
        model = ImageSubmission
        fields=("caption","image")
