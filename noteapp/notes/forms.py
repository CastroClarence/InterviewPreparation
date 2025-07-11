from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Note

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control input', 'name': 'username'}))
    password = forms.CharField(label='Password', max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control input validator', 'name': 'password'}))

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
