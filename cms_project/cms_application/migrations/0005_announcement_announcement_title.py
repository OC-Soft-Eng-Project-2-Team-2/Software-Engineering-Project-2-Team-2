# Generated by Django 3.0.8 on 2020-07-27 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_application', '0004_auto_20200727_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='announcement_title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
