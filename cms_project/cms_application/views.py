from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
import logging

# models inports
from .models import Announcement
from .models import Section
from .models import Assignment
from .models import Student
# Create your views here.

def deny_access_to_non_student(function=None):
    actual_decorator = user_passes_test(lambda u: u.groups.filter(name='Student').exists(), login_url='/accessdenied')
    return actual_decorator(function)

def deny_access_to_non_instructor(function=None):
    actual_decorator = user_passes_test(lambda u: u.groups.filter(name='Instructor').exists(), login_url='/accessdenied')
    return actual_decorator(function)

@login_required
def test(request):
    return render(request, "cms_application/home.html")

@login_required    
def home(request):
    context = {}
    context['is_student'] = request.user.groups.filter(name='Student').exists();

    announce = Announcement.objects.all()

    calendarEvents = []

    for item in announce:
        if item.posted_date.strftime("%d")[0] == "0":
            day = item.posted_date.strftime("%d")[1:]
        else:
            day = item.posted_date.strftime("%d")

        if item.posted_date.strftime("%m")[0] == "0":
            month = item.posted_date.strftime("%m")[1:]
        else:
            month = item.posted_date.strftime("%m")

        itemA = {
        'description': item.section.section_number + ": " + item.announcement_title,
        'date': item.posted_date.strftime("%x"),
        'month': month,
        'day': day,
        'year': item.posted_date.strftime("%y")
        }
        print(itemA)
        calendarEvents.append(itemA)


    context['calendarEvents'] = calendarEvents;

    announcements = []
    for item in announce:
        itemA = {
        'image': item.section.course.profile_picture_filename,
        'class': item.section.course.course_name,
        'date' : item.posted_date.strftime("%x"),
        'time' : item.posted_date.strftime("%X"),
        'title': item.announcement_title,
        'text' : item.announcement_text
            }
        announcements.append(itemA);

    context['announcements'] = announcements;

    return render(request, "cms_application/home.html", context)
    
def login(request):
    return redirect('/login/?next=/home/')

@login_required   
def aClass(request):
    context = {}
    context['is_student'] = request.user.groups.filter(name='Student').exists();
    context['is_instructor'] = request.user.groups.filter(name='Instructor').exists();

    section = Section.objects.all()

    selectedSection = section[0]

    classI = {
        "name" : selectedSection.course.course_name,
        "img" :  selectedSection.course.profile_picture_filename,
        "alt" : selectedSection.section_number,
        "syllabus" : selectedSection.syllabus_filename,
        "time": selectedSection.days_of_week + " " + selectedSection.meeting_time,
        "semester": selectedSection.semester_code,
        "credits" : selectedSection.course.credit_hours
    }
    context['class'] = classI;

    announcements = []
    announce = Announcement.objects.all()
    for item in announce:
        if item.section.section_number == selectedSection.section_number:
            itemA = {
                'image': item.section.course.profile_picture_filename,
                'class': item.section.course.course_name,
                'date' : item.posted_date.strftime("%x"),
                'time' : item.posted_date.strftime("%X"),
                'title': item.announcement_title,
                'text' : item.announcement_text
            }
            announcements.append(itemA);
    context['announcements'] = announcements;

    assignments = []
    attachments = []

    assign = Assignment.objects.all()
    for item in assign:
        if item.section.section_number == selectedSection.section_number:
            assigmentA = {
                    "title" : item.assignment_name,
                    "time" : item.due_date.strftime("%X"),
                    "date" : item.due_date.strftime("%x"),
                    "grade" : "-/100",
                    "submitted" : {
                        "time" : "",
                        "date" : ""
                    },
                    "description" : "",
                    "attachments" : item.instructions_filename,
                    "uploads" : ""
                }
            assignments.append(assigmentA)
    context["assignments"] = assignments
    
    students = []
    #    for item in selectedSection.students:
    #     student1 = {
    #         "img" : item.profile_picture_filename,
    #         "name" : item.first_name + " " + item.last_name
    #     }
    #     students.append(student1)
    student1 = {
        "img" :"https://www.demilked.com/magazine/wp-content/uploads/2019/04/5cb6d34f775c2-stock-models-share-weirdest-stories-photo-use-102-5cb5c725bc378__700.jpg",
        "name" : "Lesly"
    }
    student2 = {
        "img" :"https://footage.framepool.com/shotimg/qf/792533153-chin-finger-well-dressed-thinking.jpg",
        "name" : "Shaun"
    }
    student3 = {
        "img" :"https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRLxiGWaNSlSrHizul_Zbdf_L1EdHpNlddeRA&usqp=CAU",
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

    return render(response, "cms_application/submissions.html", context)


@login_required

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