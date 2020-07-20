from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(response):
    return render(response, "cms_application/home.html", {"UserName":"TestName"})
    
def login(response):
    return HttpResponse("<h1>Login</h1>")

def aClass(response):
    return render(response, "class.html", {"UserName":"TestName"})
