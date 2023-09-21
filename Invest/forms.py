from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



class ProfilePicForm(forms.ModelForm):
    profile_image = forms.ImageField()

    class Meta:
        model = Profile
        fields = ['profile_image']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta():
        model = User 
        fields = ['username','email','password1' ,'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)