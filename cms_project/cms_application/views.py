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
from .models import StudentAssignment
from .models import Enrollment
from .models import Professor
# Create your views here.

def sidebarInit(request):
    context = {}
    sidebar = []
    
    stud = Student.objects.all()[0]
    prof = Professor.objects.all()[0]
    enrolm = Enrollment.objects.all().filter(student=stud)

    for item in enrolm:
        classA = {
            'name' : item.section.course.course_name
        }
        sidebar.append(classA)
    context['sidebar'] = sidebar;

    context['is_student'] = request.user.groups.filter(name='student').exists();
    context['is_instructor'] = request.user.groups.filter(name='instructor').exists();

    if context['is_student']:
        context['userPfpUrl'] = stud.profile_picture_location;
    else:
        context['userPfpUrl'] = prof.profile_picture_location;
    
    return context

def deny_access_to_non_student(function=None):
    actual_decorator = user_passes_test(lambda u: u.groups.filter(name='student').exists(), login_url='/accessdenied')
    return actual_decorator(function)

def deny_access_to_non_instructor(function=None):
    actual_decorator = user_passes_test(lambda u: u.groups.filter(name='instructor').exists(), login_url='/accessdenied')
    return actual_decorator(function)

@login_required
def test(request):
    return render(request, "cms_application/home.html")

@login_required    
def home(request):
    context = sidebarInit(request)
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
        calendarEvents.append(itemA)


    context['calendarEvents'] = calendarEvents;

    announcements = []
    for item in announce:
        itemA = {
        'image': item.section.course.profile_picture_location,
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
    context = sidebarInit(request)

    stud = Student.objects.all()[0]
    enrolm = Enrollment.objects.all().filter(student=stud)[0]

    section = Section.objects.all()
    selectedSection = section[0]

    classI = {
        "name" : selectedSection.course.course_name,
        "img" :  selectedSection.course.profile_picture_location,
        "alt" : selectedSection.section_number,
        "syllabus" : selectedSection.syllabus_location,
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
                'image': item.section.course.profile_picture_location,
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
                    "attachments" : item.instructions_location,
                    "uploads" : ""
                }
            assignments.append(assigmentA)
    context["assignments"] = assignments

    gradeA = {
        'current' : 94, #enrolm.current_grade(),
        'final' : 94 #enrolm.current_grade()
    }
    context["grade"] = gradeA
    
    students = []
    for item in selectedSection.students.all():
        student1 = {
            "img" : item.profile_picture_location,
            "name" : item.first_name + " " + item.last_name
        }
        students.append(student1)
    context["students"] = students

    return render(request, "cms_application/class.html", context)

@login_required
@deny_access_to_non_instructor  
def assignmentlist(response):
    context = sidebarInit()
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

    classI = {
        "name" : selectedSection.course.course_name,
        "img" :  selectedSection.course.profile_picture_location,
        "alt" : selectedSection.section_number,
        "syllabus" : selectedSection.syllabus_location,
        "time": selectedSection.days_of_week + " " + selectedSection.meeting_time,
        "semester": selectedSection.semester_code,
        "credits" : selectedSection.course.credit_hours
    }
    context['class'] = classI;

    return render(response, "cms_application/submissions.html", context)


@login_required
@deny_access_to_non_student
def grades(request):
    context = sidebarInit(request)

    stud = Student.objects.all()[0]
    studAssign = StudentAssignment.objects.all().filter(student=stud)

    assignments = []
    for item in studAssign:
        assignA = {
            'course' : item.assignment.section.course.course_name,
            'name' : item.assignment.assignment_name,
            'grade': item.assignment_grade
        }
        assignments.append(assignA)
    context["assignments"] = assignments

    enrolm = Enrollment.objects.all().filter(student=stud)
    classes = []
    grade = ""
    for item in enrolm:
        curr = 94
        if curr >= 90:
            grade = "A"
        elif curr >= 80:
            grade = "B"
        elif curr >= 70:
            grade = "C"
        elif curr >= 60:
            grade = "D"
        else:
            grade = "F"
    
        classA = {
            'name' : item.section.course.course_name,
            'grade' : curr,
            'percentage': curr,
            'letter' : grade
        }
        classes.append(classA)
    context["classes"] = classes
    return render(request, "cms_application/grades.html", context)

@login_required
@deny_access_to_non_instructor   
def submissions(request):
    context = sidebarInit(request)
    return render(request, "cms_application/submissions.html")
    return render(request, "cms_application/class.html", {"UserName":"TestName"})
    
def accessdenied(request):
    context = sidebarInit(request)
    return render(request, "cms_application/accessdenied.html")