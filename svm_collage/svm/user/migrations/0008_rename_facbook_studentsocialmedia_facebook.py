# Generated by Django 4.2.5 on 2023-12-12 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentsocialmedia',
            old_name='facbook',
            new_name='facebook',
        ),
    ]