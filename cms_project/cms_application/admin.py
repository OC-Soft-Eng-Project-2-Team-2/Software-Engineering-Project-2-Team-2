from django import forms
from django.contrib import admin
from .models import Student, Professor, Course, Section, Assignment, Announcement, Enrollment, StudentAssignment

admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Assignment)
admin.site.register(Announcement)
admin.site.register(Enrollment)
admin.site.register(StudentAssignment)