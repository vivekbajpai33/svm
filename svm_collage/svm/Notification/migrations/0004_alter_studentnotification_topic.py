# Generated by Django 4.2.5 on 2023-12-12 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notification', '0003_alter_studentnotification_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentnotification',
            name='topic',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
