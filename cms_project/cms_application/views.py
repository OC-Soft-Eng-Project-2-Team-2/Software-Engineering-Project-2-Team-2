from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    return render(request,"home.html")
    


# def login(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']
        
#         user=auth.authenticate(username=username,password=password)


#         return render(request,"login.html")
        
