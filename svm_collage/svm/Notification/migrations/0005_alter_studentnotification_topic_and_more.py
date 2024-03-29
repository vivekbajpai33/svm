# Generated by Django 4.2.5 on 2023-12-12 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notification', '0004_alter_studentnotification_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentnotification',
            name='topic',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='studentnotification',
            name='topic_img',
            field=models.ImageField(blank=True, null=True, upload_to='notification_img'),
        ),
    ]
