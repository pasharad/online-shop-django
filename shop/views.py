from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Categorys

# Create your views here.



def index(request):
    categorys = Categorys.objects.all
    content = render(request, 'index.html', {'categorys':categorys})
    return HttpResponse(content)