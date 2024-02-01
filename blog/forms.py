from .models import Comment, Profile
from django import forms



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'about_user']