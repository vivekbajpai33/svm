from captcha.fields import CaptchaField
from django.db import models
from django.contrib.auth.models import User


class StudentSocialMedia(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    facebook = models.CharField(max_length=500, null=True, blank=True)
    instagram = models.CharField(max_length=500, null=True, blank=True)
    twitter = models.CharField(max_length=500, null=True, blank=True)
    github = models.CharField(max_length=500, null=True, blank=True)
    snapchat = models.CharField(max_length=500, null=True, blank=True)

    # def __str__(self):
    #     return self.student

class StudentStories(models.Model):
    student = models.CharField(max_length=200, null=True, blank=True)
    img =  models.FileField(upload_to='notification_img', null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    pen = models.BooleanField(default = False, null=True, blank=True)
    creted_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    
    











   
    