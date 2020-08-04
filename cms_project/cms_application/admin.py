from django.contrib import admin

from .models import Student,Professor,Admin,Course

# Register your models here.
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Admin)
admin.site.register(Course)
