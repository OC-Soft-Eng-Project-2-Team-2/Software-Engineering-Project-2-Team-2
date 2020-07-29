from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

#@login_required
def home(request):
    return render(request, "cms_application/home.html")
    
def login(response):
    return render(response, "registration/login.html")

def aClass(response):
    return render(response, "cms_application/class.html")

def grades(response):
    return render(response, "cms_application/index.html")

def assignmentlist(response):
    return render(response, "cms_application/assignmentList.html")
