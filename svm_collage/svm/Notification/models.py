from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.
# this model for a collage and student notification
class StudentNotification(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    topic = models.CharField(max_length=200, null=True)
    details = models.TextField(null=True, blank=True)
    topic_img = models.ImageField(upload_to='notification_img', null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True, auto_created=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.topic)
        super(StudentNotification, self).save(*args, **kwargs)