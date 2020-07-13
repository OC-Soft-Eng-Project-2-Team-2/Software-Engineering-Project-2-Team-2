from django.db import models
from django.contrib.auth.models import User  # for authentication & authorization purposes


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    student_id = models.CharField(max_length=7, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    major = models.CharField(max_length=100)

    sections = models.ManyToManyField(
        'Section',
        through='Enrollment',
        through_fields=('student', 'section')
    )
    assignments = models.ManyToManyField(
        'Assignment',
        through='StudentAssignment',
        through_fields=('student', 'assignment')
    )            

    @property
    def student_data_folder_name(self):
        """This is the folder where a student's profile image will be stored, as well as assignment-submission subfolders for all enrolled sections."""
        return "cms_application/static/students/" + self.student_id + '/'

    @property
    def classification(self):
        credit_hours_completed = 0

        if len(self.sections) != 0:
            for s in self.sections:
                if s.status in ['REGISTERED', 'REGISTERED_PF'] and s.final_letter_grade in ['A', 'B', 'C', 'D', 'P']:
                    credit_hours_completed += s.section.course.credit_hours

        if credit_hours_completed < 30:
            return 'FRESHMAN'
        elif credit_hours_completed < 60:
            return 'SOPHOMORE'
        elif credit_hours_completed < 90:
            return 'JUNIOR'
        elif credit_hours_completed < 120:
            return 'SENIOR'
        else:
            return 'GRADUATE'

    @property
    def cumulative_gpa(self):
        sum = 0

        if len(self.sections) != 0:
            for s in self.sections:
                credit_hours = 0
                grade_points = 0

                if s.status in ['REGISTERED', 'REGISTERED_PF']:
                    credit_hours = s.section.course.credit_hours

                if s.final_letter_grade == 'A':
                    grade_points = 4
                elif s.final_letter_grade == 'B':
                    grade_points = 3
                elif s.final_letter_grade == 'C':
                    grade_points = 2
                elif s.final_letter_grade == 'D':
                    grade_points = 1

                sum += credit_hours * grade_points
        
        return round((sum / 4.0), 2)

    def __str__(self):
        return self.last_name + ', ' + self.first_name + ' (' + self.student_id + ')'
                

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    faculty_id = models.CharField(max_length=7, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    
    def __str__(self):
        return self.last_name + ', ' + self.first_name + ' (' + self.faculty_id + '); ' + self.department


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    staff_id = models.CharField(max_length=7, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.last_name + ', ' + self.first_name + ' (' + self.staff_id + '); Administrator'


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    department_code = models.CharField(max_length=4)
    course_number = models.CharField(max_length=4)
    credit_hours = models.IntegerField()
    course_description = models.CharField(max_length=1000)

    @property
    def full_course_code(self):
        return self.department_code + '-' +  self.course_number

    def __str__(self):
        return self.course_name + ' (' + self.full_course_code + ')'

    class Meta:
        """Enforces that no two courses have the same full_course_code"""
        unique_together=('department_code', 'course_number')


class Section(models.Model):
    section_number = models.CharField(max_length=2)
    classroom = models.CharField(max_length=9)
    days_of_week = models.CharField(max_length=10)
    meeting_time = models.CharField(max_length=20)
    semester_code = models.CharField(max_length=6)
    start_date = models.DateField()
    end_date = models.DateField()

    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
    professor = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True)

    students = models.ManyToManyField(
        'Student',
        through='Enrollment',
        through_fields=('section', 'student')
    )

    @property
    def full_section_code(self):
        return self.course.full_course_code + '-' + self.section_number + '_' + self.semester_code

    @property
    def student_data_subfolder_name(self):
        """This is the subfolder under a student's data_folder where assignment-submissions for this section will be stored."""
        return self.full_section_code + '/'

    @property
    def section_data_folder_name(self):
        """This is the folder where the syllabus, all assignment instructions, and any other shared resources used for this section will be stored."""
        return "cms_application/static/sections/" + self.full_section_code + '/'

    def __str__(self):
        return self.full_section_code

    class Meta:
        """Enforces that no two sections have the same full_section_code"""
        unique_together=('course', 'section_number', 'semester_code')


class Assignment(models.Model):
    section = models.ForeignKey('Section', on_delete=models.SET_NULL, null=True)
    assignment_name = models.CharField(max_length=100)
    due_date = models.DateField()
    
    students = models.ManyToManyField(
        'Student',
        through='StudentAssignment',
        through_fields=('assignment', 'student')
    )            

    @property
    def instructions_folder_name(self):
        """This is the subfolder under the section folder where the assignment instructions will be stored"""
        return self.section.section_data_folder_name + self.assignment_name + '/'

    @property
    def student_data_subfolder_name(self):
        """This is the subfolder under a student's data where the submission file for this assignment will be stored."""
        return self.student_data_subfolder_name + self.assignment_name + '/'

    def __str__(self):
        return str(self.section) + ' - ' + self.assignment_name

    class Meta:
        """Enforces that no two assignments for the same section have the same name"""
        unique_together = ('section', 'assignment_name')


class Enrollment(models.Model):
    """Status tells the relationship between the student and the section, letter_grade tells the student's performance in the section.
    
        status='DROPPED' is used if the student drops the class any time before the school's scheduled 'last day to drop without a W'; no letter_grade is recorded.
        letter_grade='W' is used if the student drops the class any time after the above date but before the school's 'last day to drop with a W'.
        """
    status = models.CharField(max_length=13)  # REGISTERED, REGISTERED_PF, AUDITED, WAITLISTED, or DROPPED
    midterm_letter_grade = models.CharField(max_length=1, null=True) # manually entered by professor, can be: A, B, C, D, F, P (pass), or W (withdrawal)
    final_letter_grade = models.CharField(max_length=1, null=True) # manually entered by professor, can be any of the options available to midterm_letter_grade or I (incomplete)

    student = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True)
    section = models.ForeignKey('Section', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.student) + ' enrolled in ' + str(self.section.full_section_code) + '; Status: ' + self.status


class StudentAssignment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True)
    assignment = models.ForeignKey('Assignment', on_delete=models.SET_NULL, null=True)
    assignment_grade = models.FloatField()  # manually entered by professor
    submission_file_name = models.CharField(max_length=50, null=True)  # the name of the file the student uploads; should be overwritten by subsequent submissions

    @property
    def student_assignment_submission_location(self):
        """This is the full path to the folder where the student's submission for the assignment can be found"""
        return self.student.student_data_folder_name + self.assignment.student_data_subfolder_name + self.submission_file_name


    def __str__(self):
        return str(self.assignment) + ': ' + str(self.student)



# the directory tree is probably borked to heck, and we need enums to control allowable values in the Enrollment status & grade fields (customize the django-admin interface)