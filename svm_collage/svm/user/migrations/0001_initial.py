# Generated by Django 4.2.5 on 2023-11-25 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100, null=True)),
                ('otp', models.IntegerField()),
                ('userotp', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('number', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
