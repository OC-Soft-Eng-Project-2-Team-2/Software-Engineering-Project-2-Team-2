from django.contrib import admin
from .models import Student, Professor, Course, Section, Assignment, Announcement, Enrollment, StudentAssignment, CalendarEvent

<<<<<<< Updated upstream
from .models import Student,Professor,Admin,Course

# Register your models here.
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Admin)
admin.site.register(Course)
=======
admin.site.register(Student)

admin.site.register(Professor)

admin.site.register(Course)

admin.site.register(Section)

admin.site.register(Assignment)

admin.site.register(Announcement)

admin.site.register(Enrollment)

admin.site.register(StudentAssignment)

admin.site.register(CalendarEvent)
>>>>>>> Stashed changes
