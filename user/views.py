import math
import random
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import LoginForm, ProfileForm, RegistrationForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import User
from django.contrib.auth.views import TemplateView
from django.http import HttpResponse
from django.core.mail import send_mail

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
    #         user = authenticate(username=username, password=password)
    #         if user is not None:
    #             login(request, user)
    #             return redirect('http://127.0.0.1:8000/shop/index') # replace 'home' with your app's home page URL name
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/account/login')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('http://127.0.0.1:8000/shop/index') # replace 'home' with your app's home page URL name
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
    
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            redirect('http://127.0.0.1:8000/account/profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'profile.html', {'form':form})    
            




from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import LoginSerializer
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError



class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)

            username = request.data.get('username')
            password = request.data.get('password')

            if username and password:
                user = authenticate(username=username, password=password)
                login(request, user)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

def generateOTP() :
     digits = "0123456789"
     OTP = ""
     for i in range(4) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP

def send_otp(request):
     email=request.GET.get("email")
     print(email)
     o=generateOTP()
     htmlgen = '<p>Your OTP is <strong>o</strong></p>'
     send_mail('OTP request',o,settings.EMAIL_HOST_USER ,[email], fail_silently=False, html_message=htmlgen)
     print(o)
     return HttpResponse(o)