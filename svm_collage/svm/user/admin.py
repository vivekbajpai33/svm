from django.contrib import admin
from .models import *

@admin.register(StudentSocialMedia)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id','student')
    search_fields = ['student']
    list_filter = ['student']

@admin.register(StudentStories)
class StoriesAdmin(admin.ModelAdmin):
    list_display = ('id','student','title','pen')

# Register your models here.
