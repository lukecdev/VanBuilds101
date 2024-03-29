from .models import Comment, Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)



class EditUserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'name', 'profile_image', 'about_user']