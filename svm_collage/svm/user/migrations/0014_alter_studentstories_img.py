# Generated by Django 4.2.5 on 2023-12-16 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_rename_student_studentstories_student_story'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentstories',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='notification_img'),
        ),
    ]
