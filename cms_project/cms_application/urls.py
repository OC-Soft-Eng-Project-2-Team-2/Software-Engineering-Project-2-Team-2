from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("class/", views.aClass, name="class"),
    path("grades/", views.grades, name="grades")
]