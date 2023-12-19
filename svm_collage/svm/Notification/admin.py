from django.contrib import admin
from .models import *



@admin.register(StudentNotification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id','student','topic')

# Register your models here.
