from django import forms
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password', 'name': 'password'}))
    rememberme = forms.BooleanField(label="Remember Me",
                           widget=forms.CheckboxInput(attrs={'class': 'checkbox active', 'name': 'rememberme'}))
