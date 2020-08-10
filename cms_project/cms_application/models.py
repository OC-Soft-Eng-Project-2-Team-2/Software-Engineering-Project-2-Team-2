from django.db import models
from django.contrib.auth.models import User  # for authentication & authorization purposes

import datetime


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    staff_id = models.CharField(max_length=7, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    def str(self):
        return self.last_name + ', ' + self.first_name + ' (' + self.staff_id + '); Administrator'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    student_id = models.CharField(max_length=7, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    major = models.CharField(max_length=100)
    
    profile_picture_filename = models.CharField(max_length=50, null=True, blank=True)

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
        """This is the folder where a student's profile image and uploaded coursework will be stored."""
        return "../../static/students/" + self.student_id + '/'


    @property
    def profile_picture_location(self):
        """This is the full filepath to the student's profile image."""
        if self.profile_picture_filename is None:
            return "../../static/cms_application/account icon.png"
        else:
            return self.student_data_folder_name + self.profile_picture_filename

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

    @property
    def current_semester_gpa(self):
        today = datetime.date.today()
        current_enrollments = self.sections.filter(start_date <= today and end_date >= today)
        grade_points = 0
        if current_enrollments:
            for e in current_enrollments:
                if e.current_grade >= 90.00:
                    grade_points = grade_points + (4 * e.section.course.credit_hours)
                elif e.current_grade >= 80.00:
                    grade_points = grade_points + (3 * e.section.course.credit_hours)
                elif e.current_grade >= 70.00:
                    grade_points = grade_points + (2 * e.section.course.credit_hours)
                elif e.current_grade >= 60.00:
                    grade_points = grade_points + e.section.course.credit_hours
                else:
                    pass  # don't add anything in the event of a failing grade
        return round(grade_points / 4.0, 2)

    def __str__(self):
        return self.last_name + ', ' + self.first_name + ' (' + self.student_id + ')'
                

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    faculty_id = models.CharField(max_length=7, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    department = models.CharField(max_length=100)

    profile_picture_filename = models.CharField(max_length=50, null=True, blank=True)

    @property
    def profile_picture_location(self):
        """This is the filepath to the professor's profile image."""
        if self.profile_picture_filename is None:
            return "../../static/cms_application/account icon.png"
        else:
            return "../../static/professors/" + self.faculty_id + "/" + self.profile_picture_filename

    
    def __str__(self):
        return self.last_name + ', ' + self.first_name + ' (' + self.faculty_id + '); ' + self.department


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    department_code = models.CharField(max_length=4)
    course_number = models.CharField(max_length=4)
    credit_hours = models.IntegerField()
    course_description = models.CharField(max_length=1000)

    profile_picture_filename = models.CharField(max_length=50, null=True, blank=True)

    @property
    def profile_picture_location(self):
        """This is the filepath to the course image."""
        if self.profile_picture_filename is None:
            return "../../static/cms_application/Class icon white.png"
        else:
            return "../../static/courses/" + self.full_course_code + "/" + self.profile_picture_filename

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

    syllabus_filename = models.CharField(max_length=50, null=True, blank=True)

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
        """This is the folder where the syllabus and all assignment instructions used for this section will be stored."""
        return "../../static/sections/" + self.full_section_code + '/'

    @property
    def syllabus_location(self):
        """This is the filepath to the section syllabus."""
        if self.syllabus_filename is None:
            return None
        else:
            return self.section_data_folder_name + self.syllabus_filename

    def __str__(self):
        return self.full_section_code

    class Meta:
        """Enforces that no two sections have the same full_section_code"""
        unique_together=('course', 'section_number', 'semester_code')


class Announcement(models.Model):
    section = models.ForeignKey('Section', on_delete=models.SET_NULL, null=True)
    posted_date = models.DateField()
    announcement_title = models.CharField(max_length=100)
    announcement_text = models.CharField(max_length=1000)

    def __str__(self):
        return self.announcement_title + ' (' + str(self.posted_date) + '): ' + self.announcement_text[:100]


class Assignment(models.Model):
    section = models.ForeignKey('Section', on_delete=models.SET_NULL, null=True)
    assignment_name = models.CharField(max_length=100)
    due_date = models.DateField()
    
    students = models.ManyToManyField(
        'Student',
        through='StudentAssignment',
        through_fields=('assignment', 'student')
    )            

    instructions_filename = models.CharField(max_length=50, null=True, blank=True)

    @property
    def instructions_location(self):
        """This is the location where the instructions for the assignment will be stored"""
        if self.instructions_filename is None:
            return None
        else:            
            return self.section.section_data_folder_name + self.assignment_name + '/' + self.instructions_filename

    @property
    def student_data_subfolder_name(self):
        """This is the subfolder under a student's data where the submission file for this assignment will be stored."""
        return self.section.student_data_subfolder_name + self.assignment_name + '/'

    def __str__(self):
        return str(self.section) + ' - ' + self.assignment_name

    class Meta:
        """Enforces that no two assignments for the same section have the same name"""
        unique_together = ('section', 'assignment_name')


class Enrollment(models.Model):
    """Status tells the relationship between the student and the section, letter_grade tells the student's performance in the section.
    
        status='DROPPED' is used if the student drops the class any time before the school's scheduled 'last day to drop without a W'; no letter_grade is recorded.
        final_letter_grade='W' is used if the student drops the class any time after the above date but before the school's 'last day to drop with a W'.
        """
    status = models.CharField(
        max_length=4,
        choices=[
            ('WAIT', 'Waitlisted'),
            ('REG', 'Registered'),
            ('RPF', 'Registered Pass/Fail'),
            ('AUD', 'Auditing'),
            ('DROP', 'Dropped')
        ],
        default='WAIT'
    )

    student = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True)
    section = models.ForeignKey('Section', on_delete=models.SET_NULL, null=True)

    @property
    def current_grade(self):
        current_section_student_assignments = self.student.assignments.filter(assignment.section==self.section)
        sum_of_grades = 0
        if current_section_student_assignments:
            for a in current_section_student_assignments:
                sum_of_grades = sum_of_grades + a.assignment_grade
        return round(sum_of_grades / 100.00, 2)

    def __str__(self):
        return str(self.student) + ' enrolled in ' + str(self.section.full_section_code) + '; Status: ' + self.status


class StudentAssignment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True)
    assignment = models.ForeignKey('Assignment', on_delete=models.SET_NULL, null=True)
    assignment_grade = models.DecimalField(max_digits=5, decimal_places=2)  # manually entered by professor, must be between 0.00 and 100.00
    submission_filename = models.CharField(max_length=50, null=True, blank=True)

    @property
    def student_data_subfolder_name(self):
        return self.student.student_data_folder_name + self.assignment.student_data_subfolder_name + '/'


    @property
    def student_assignment_submission_location(self):
        """This is the full path to the folder where the student's submission for the assignment can be found"""
        return self.student_data_subfolder_name + self.submission_filename

    def __str__(self):
        return str(self.assignment) + ': ' + str(self.student)



#######################################################################################################################
#  Any field ending with '_filename' gets its data from a file upload, and should be overwritten by subsequent uploads
#    (e.g. if a student goes to the place to upload a profile pic, uploads one, and then uploads another, the new one
#    should overwrite whatever data was in the field, so the old one is gone even if the file is still there. Ideally
#    the upload process would first delete the old one, THEN save the new, but it's not strictly required.)
#
#  Any @property ending with _'subfolder_name' is used in calculating the final location of static files related to the
#    object that has the @property. When you SAVE a file, the value in this property is the folder you will be saving
#    the file into.
#
#  Any @property ending with '_location' is the actual location of a file; you will use this @property to get the
#    location of any file you want to DISPLAY or DOWNLOAD.
#
#
# SUMMARY
# If this all works together correctly, the steps are as follows:
#
# File Upload --
#  1) A user submits a File to upload, which is linked to an Object.
#              (A File is a .png, .jpg, .doc/.docx, .txt, or .pdf document. Other MIME types are tedious to support.)
#              (Objects that can have files are: Student, Professor, Course, Section, Assignment, or StudentAssignment)
#  2) The system checks the Object's corresponding '_location' @property
#     2a) If the @property does not return a 'None' value, the file at the location *should*, in an ideal world, be
#         deleted before proceeding.
#     2b) If the @property did return a 'None' value, or if the old file at the location has been deleted, (or, in a
#         non-ideal world, if we have chosen to simply ignore old files), the system proceeds to step 3.
#  3) The system gets the name of the File, and stores it in the Object's '_filename' field, overwriting any previous
#     value.
#  4) The system saves the File to the subfolder specified in the Object's '_subfolder_name' @property (IF MORE THAN ONE
#     OF THESE EXIST, use the one that is called by the '_location' @property), overwriting any previous file which may
#     have existed under the same name in that subfolder.
#
# File Display --
#  1) A user accesses a page where the File would be displayed.
#  2) The system uses the value in the Object's '_location' @property to locate the File.
#     2a) If, for some reason, the '_location' @property returns 'None', the system should display a "not found" message.
#     2b) Else, the system should load and display the File.
#         2b.1) If downloading the File is possible, that option is offered.
#######################################################################################################################
