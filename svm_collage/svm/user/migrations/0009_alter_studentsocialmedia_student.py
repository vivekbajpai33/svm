# Generated by Django 4.2.5 on 2023-12-15 06:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0008_rename_facbook_studentsocialmedia_facebook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsocialmedia',
            name='student',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
