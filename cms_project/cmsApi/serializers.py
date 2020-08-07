from django.contrib.auth.models import User, Group
from cms_application.models import Student,Professor,Admin,Course,Section,Announcement,Assignment, Enrollment,StudentAssignment,Admin
from rest_framework import serializers




# Serializers define the API representation.

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class  StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['user','student_id', 'first_name', 'last_name','email', 'major','sections','assignments']


class  ProfessorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =Professor
        fields = ['faculty_id', 'first_name', 'last_name','email', 'department']


class AdminSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model =Admin
        fields = ['user', 'staff_id', 'first_name','last_name', 'email']

class CourseSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model =Course
        fields = ['course_name', 'department_code', 'course_number','credit_hours', 'course_description'] 


class SectionSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model =Section
        fields = ['section_number', 'classroom', 'days_of_week','meeting_time', 'semester_code','start_date','end_date','course','professor','syllabus_filename','students']   


class AnnouncementSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model =Announcement
        fields = ['section', 'posted_date', 'announcement_title','announcement_text']  



class AssignmentSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model =Assignment
        fields = ['section', 'assignment_name', 'due_date','students','instructions_filename'] 





class EnrollmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['status', 'student', 'section']




class StudentAssignmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentAssignment
        fields = ['student', 'assignment', 'assignment_grade','submission_filename']


