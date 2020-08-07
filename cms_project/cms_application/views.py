from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
import logging
# Create your views here.

@login_required
def test(request):
    return render(request, "cms_application/home.html")

@login_required    
def home(request):

    context = {}
    calendarEvents = []

    context['is_student'] = request.user.groups.filter(name='Student').exists();

    #Test info, replace with info for student from database
    event1 = {
        'description': "TEST: This is a test description 1",
        'date':"7/13/20",
        'month': "7",
        'day': "13",
        'year': '20'
        }
    event2 = {
        'description': "TEST: This is a test description 2",
        'date':"7/23/20",
        'month': "7",
        'day': "23",
        'year': '20'
        }
    event3= {
        'description': "TEST: This is a test description 3",
        'date':"7/27/20",
        'month': "7",
        'day': "27",
        'year': '20'
        }

    calendarEvents.append(event1)
    calendarEvents.append(event2)
    calendarEvents.append(event3)
    context['calendarEvents'] = calendarEvents;

    announcements = []
    item1 = {
        'image': "https://cf-images.us-east-1.prod.boltdns.net/v1/static/5660549791001/d8e5eb81-e27a-4bbf-8324-1090d1a5542e/8e2312dd-bba2-4601-954f-8b8698c3f347/1000x563/match/image.jpg",
        'class': "YEET 101 - Intro to Yeet",
        'date' : "7/15/2020",
        'time' : "4:19 PM",
        'title': "Yeet or be Yeeted",
        'text' : "Yeet"
    }

    item2 = {
        'image': "https://cf-images.us-east-1.prod.boltdns.net/v1/static/5660549791001/d8e5eb81-e27a-4bbf-8324-1090d1a5542e/8e2312dd-bba2-4601-954f-8b8698c3f347/1000x563/match/image.jpg",
        'class': "YEET 101 - Intro to Yeet",
        'date' : "7/16/2020",
        'time' : "4:19 PM",
        'title': "Yeet or be Yeeted",
        'text' : "Yeet"
    }

    item3 = {
        'image': "https://cf-images.us-east-1.prod.boltdns.net/v1/static/5660549791001/d8e5eb81-e27a-4bbf-8324-1090d1a5542e/8e2312dd-bba2-4601-954f-8b8698c3f347/1000x563/match/image.jpg",
        'class': "YEET 101 - Intro to Yeet",
        'date' : "7/17/2020",
        'time' : "4:19 PM",
        'title': "Yeet or be Yeeted",
        'text' : "Yeet"
    }

    announcements.append(item1);
    announcements.append(item2);
    announcements.append(item3);
    context['announcements'] = announcements;

    return render(request, "cms_application/home.html", context)
    
def login(request):
    return redirect('/login/?next=/home/')

@login_required   
def aClass(request):
    context = {}
    context['is_student'] = request.user.groups.filter(name='Student').exists();
    context['is_instructor'] = request.user.groups.filter(name='Instructor').exists();

    classI = {
        "name" : "Test Name",
        "img" : "https://i.imgflip.com/2xnbeb.jpg",
        "alt" : "Waaa",
        "syllabus" : "/class",
        "time": "MTWTHF 12:00AM - 12:00PM",
        "semester": "2020 Fall Session 1",
        "credits" : "12"
    }
    context['class'] = classI;

    announcements = []
    item1 = {
        'image': "https://cf-images.us-east-1.prod.boltdns.net/v1/static/5660549791001/d8e5eb81-e27a-4bbf-8324-1090d1a5542e/8e2312dd-bba2-4601-954f-8b8698c3f347/1000x563/match/image.jpg",
        'class': "YEET 101 - Intro to Yeet",
        'date' : "7/15/2020",
        'time' : "4:19 PM",
        'title': "Yeet or be Yeeted",
        'text' : "Yeet"
    }

    item2 = {
        'image': "https://cf-images.us-east-1.prod.boltdns.net/v1/static/5660549791001/d8e5eb81-e27a-4bbf-8324-1090d1a5542e/8e2312dd-bba2-4601-954f-8b8698c3f347/1000x563/match/image.jpg",
        'class': "YEET 101 - Intro to Yeet",
        'date' : "7/16/2020",
        'time' : "4:19 PM",
        'title': "Yeet or be Yeeted",
        'text' : "Yeet"
    }

    item3 = {
        'image': "https://cf-images.us-east-1.prod.boltdns.net/v1/static/5660549791001/d8e5eb81-e27a-4bbf-8324-1090d1a5542e/8e2312dd-bba2-4601-954f-8b8698c3f347/1000x563/match/image.jpg",
        'class': "YEET 101 - Intro to Yeet",
        'date' : "7/17/2020",
        'time' : "4:19 PM",
        'title': "Yeet or be Yeeted",
        'text' : "Yeet"
    }

    announcements.append(item1);
    announcements.append(item2);
    announcements.append(item3);
    context['announcements'] = announcements;

    assignments = []
    attachments = []
    attach1 = {
        "url" : "Waluigi #1",
        "title" : "Waluigi #1"
    }
    attachments.append(attach1)

    upload = []
    up1 = {
        "url" : "Waluigi #1",
        "title" : "Waluigi #1 Done"
    }
    upload.append(up1)

    assigment1 = {
        "title" : "Homework 1",
        "time" : "11:59PM",
        "date" : "7/30/2020",
        "grade" : "-/100",
        "submitted" : {
            "time" : "10:00 AM",
            "date" : "7/25/2020"
        },
        "description" : "Chp 1 questions 1-5, A-Z",
        "attachments" : attachments,
        "uploads" : upload
    }

    assigment2 = {
        "title" : "Homework 1",
        "time" : "11:59PM",
        "date" : "7/30/2020",
        "grade" : "-/100",
        "submitted" : {
            "time" : "10:00 AM",
            "date" : "7/25/2020"
        },
        "description" : "Chp 3 questions 7-16, A-Z",
        "attachments" : attachments,
        "uploads" : upload
    }

    assignments.append(assigment1);
    assignments.append(assigment2);
    context["assignments"] = assignments

    students = []
    student1 = {
        "img" :"https://upload.wikimedia.org/wikipedia/en/thumb/8/8b/Purplecom.jpg/200px-Purplecom.jpg",
        "name" : "Purple"
    }
    student2 = {
        "img" :"https://pyxis.nymag.com/v1/imgs/07f/762/6ec01dddd29c0a9d9895b71c20c0bd911d-alien.rsquare.w700.jpg",
        "name" : "Shaun"
    }
    student3 = {
        "img" :"https://cdn0.wideopenpets.com/wp-content/uploads/2019/10/Fish-Names-770x405.png",
        "name" : "Tony"
    }
    students.append(student1)
    students.append(student2)
    students.append(student3)
    context["students"] = students

    return render(request, "cms_application/class.html", context)

@login_required  
@deny_access_to_non_instructor 
def assignmentlist(response):
    context = {}
    submissions = []

    sub1 = {
        'submittor' : "Shaun",
         'attachments' : [{'name' : "Essay.doc",
                            'url' : 'Essay.doc'}],
        'date' : "07/08/2020",
        'time' : "8:02 AM"
    }

    sub2 = {
        'submittor' : "Kyle",
        'attachments' : [{'name' : "paper.doc",
                            'url' : 'paper.doc'}],
 
        'date' : "07/12/2020",
        'time' : "3:42 AM"

    }

    sub3 = {
        'submittor' : "Lily",
        'attachments' : [{'name' : "Dissertation on the being of man.doc.doc",
                            'url' : 'Dissertation on the being of man.doc.doc'}],
        'date' : "07/12/2020",
        'time' : "1:59 PM"
    }

    submissions.append(sub1);
    submissions.append(sub2);
    submissions.append(sub3);
    context["submissions"] = submissions

    classD = {
        'name' : 'Class Name',
        'img' : 'https://us.123rf.com/450wm/stockbroker/stockbroker1408/stockbroker140802515/31050918-class-of-university-students-using-laptops-in-lecture.jpg?ver=6',
        'time' : 'MWF 8:00 AM',
        'semester' : '2020 Summer Session 1'
    }

    context["class"] = classD

    return render(response, "cms_application/assignmentList.html", context)
def deny_access_to_non_student(function=None):
    actual_decorator = user_passes_test(lambda u: u.groups.filter(name='Student').exists(), login_url='/accessdenied')
    return actual_decorator(function)

def deny_access_to_non_instructor(function=None):
    actual_decorator = user_passes_test(lambda u: u.groups.filter(name='Instructor').exists(), login_url='/accessdenied')
    return actual_decorator(function)

@login_required
@deny_access_to_non_student
def grades(request):
    context = {}
    context['is_student'] = request.user.groups.filter(name='Student').exists();
    grades = []

    grade1 = {
        'name': 'Course I',
        'grade': '50/100',
        'percentage': 50, 
        'letter': 'F',
        'assignments': [
            {'name': 'Assignment1', 'grade': '50/100'},
            {'name': 'Assignment2', 'grade': '50/100'},
            {'name': 'Assignment3', 'grade': '50/100'},
            {'name': 'Assignment4', 'grade': '50/100'},
            {'name': 'Assignment5', 'grade': '50/100'}
        ]
    }

    grade2 = {
        'name': 'Course II',
        'grade': '200/100',
        'percentage': 200, 
        'letter': 'A',
        'assignments': [
            {'name': 'Assignment1', 'grade': '200/100'},
            {'name': 'Assignment2', 'grade': '200/100'},
            {'name': 'Assignment3', 'grade': '200/100'},
            {'name': 'Assignment4', 'grade': '200/100'},
            {'name': 'Assignment5', 'grade': '200/100'}
        ]
    }

    grades.append(grade1)
    grades.append(grade2)
    context["grades"] = grades
    
    return render(request, "cms_application/grades.html", context)

@login_required
@deny_access_to_non_instructor   
def submissions(request):
    return render(request, "cms_application/submissions.html")
    return render(request, "cms_application/class.html", {"UserName":"TestName"})
    
def accessdenied(request):
    context = {}
    context['is_student'] = request.user.groups.filter(name='Student').exists();
    return render(request, "cms_application/accessdenied.html")