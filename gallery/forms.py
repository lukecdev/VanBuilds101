from .models import Image, ImageSubmission
from django import forms

class ImageSubmissionForm(forms.ModelForm):
    class Meta:
        model = ImageSubmission
        fields=("caption","image")
