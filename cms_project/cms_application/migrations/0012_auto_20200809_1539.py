# Generated by Django 3.0.8 on 2020-08-09 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_application', '0011_auto_20200809_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='instructions_filename',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='profile_picture_filename',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='profile_picture_filename',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='syllabus_filename',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='profile_picture_filename',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='studentassignment',
            name='submission_filename',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]