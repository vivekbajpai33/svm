# Generated by Django 4.2.5 on 2023-12-12 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notification', '0002_alter_studentnotification_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentnotification',
            name='slug',
            field=models.SlugField(auto_created=True, blank=True, null=True, unique=True),
        ),
    ]
