# Generated by Django 3.0.8 on 2020-07-12 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_name', models.CharField(max_length=100)),
                ('due_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('department_code', models.CharField(max_length=4)),
                ('course_number', models.CharField(max_length=4)),
                ('credit_hours', models.IntegerField()),
                ('course_description', models.CharField(max_length=1000)),
            ],
            options={
                'unique_together': {('department_code', 'course_number')},
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=13)),
                ('midterm_letter_grade', models.CharField(max_length=1, null=True)),
                ('final_letter_grade', models.CharField(max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('faculty_id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=100)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_number', models.CharField(max_length=2)),
                ('classroom', models.CharField(max_length=9)),
                ('days_of_week', models.CharField(max_length=10)),
                ('meeting_time', models.CharField(max_length=20)),
                ('semester_code', models.CharField(max_length=6)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_application.Course')),
                ('professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_application.Professor')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('major', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StudentAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_grade', models.FloatField()),
                ('submission_file_name', models.CharField(max_length=50, null=True)),
                ('assignment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_application.Assignment')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_application.Student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='assignments',
            field=models.ManyToManyField(through='cms_application.StudentAssignment', to='cms_application.Assignment'),
        ),
        migrations.AddField(
            model_name='student',
            name='sections',
            field=models.ManyToManyField(through='cms_application.Enrollment', to='cms_application.Section'),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='section',
            name='students',
            field=models.ManyToManyField(through='cms_application.Enrollment', to='cms_application.Student'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_application.Section'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_application.Student'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms_application.Section'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='students',
            field=models.ManyToManyField(through='cms_application.StudentAssignment', to='cms_application.Student'),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('staff_id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='section',
            unique_together={('course', 'section_number', 'semester_code')},
        ),
        migrations.AlterUniqueTogether(
            name='assignment',
            unique_together={('section', 'assignment_name')},
        ),
    ]