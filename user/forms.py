from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(label= 'نام کاربری', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}))
    password = forms.CharField(label='رمزعبور', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}))

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label= 'نام کاربری', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}))
    email = forms.EmailField(label= 'ایمیل', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}))
    first_name = forms.CharField(label='نام', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'}))
    last_name = forms.CharField(label='نام خانوادگی', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی '}))
    password1 = forms.CharField(label='رمزعبور', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمزعبور'}))
    password2 = forms.CharField(label='تکرار رمزعبور', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تکرار رمزعبور'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']