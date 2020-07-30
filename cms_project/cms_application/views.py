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
    return render(response, "registration/login.html", {"UserName":"TestName"})

def aClass(response):
    return render(response, "cms_application/class.html", {"UserName":"TestName"})

def grades(response):
    return render(
        response, 
        "cms_application/grades.html",
        {"grades": [
            {
                'name': 'Course I',
                'grade': '200/100',
                'percentage': 200, 
                'letter': 'F',
                'assignments': [
                        {'name': 'Assignment1', 'grade': '200/100'},
                        {'name': 'Assignment2', 'grade': '200/100'},
                        {'name': 'Assignment3', 'grade': '200/100'},
                        {'name': 'Assignment4', 'grade': '200/100'},
                        {'name': 'Assignment5', 'grade': '200/100'},
                ]
            },
            {
                'name': 'Course II',
                'grade': '50/100',
                'percentage': 200, 
                'letter': 'A',
                'assignments': [
                        {'name': 'Assignment1', 'grade': '200/100'},
                        {'name': 'Assignment2', 'grade': '200/100'},
                        {'name': 'Assignment3', 'grade': '200/100'},
                        {'name': 'Assignment4', 'grade': '200/100'},
                        {'name': 'Assignment5', 'grade': '200/100'},
                ]
            },
        ]}
    )    
