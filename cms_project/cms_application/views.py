from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(response):
    return HttpResponse("<h1>Class Management System</h1>")
    
def login(response):
    return HttpResponse("<h1>Login</h1>")

def aClass(response):
    return render(response, "class.html", {"UserName":"TestName"})