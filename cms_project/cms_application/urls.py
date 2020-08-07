from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="test"),
    path("home/", views.home, name="home"),
    path("class/", views.aClass, name="class"),
    path("grades/", views.grades, name="grades"),
    path("assignmentlist/", views.assignmentlist, name="assignmentList")
]