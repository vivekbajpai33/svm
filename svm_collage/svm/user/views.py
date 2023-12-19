from django.shortcuts import render,HttpResponse,redirect
import requests
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import random
from user.views import *
from user.forms import *
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
#####User Profile
from .forms import *
# from svm.settings import  EMAIL_HOST_USER
from django.http import HttpResponse
from user.email_utils import send_custom_email
import uuid
# ######## Change password
from django.contrib.auth.views import PasswordChangeView 
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy

######## Reset Password
from django.contrib.auth.views import PasswordResetView

#### change user profile
from django.contrib.auth.forms import UserChangeForm


###### user social media
from user.models import *
from Notification.models import *
##### qr genrate
import qrcode

############## New User Login page
def LoginView(request):
    if request.method== 'POST':
        Email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirm_password')
        if password==confirmpassword:
            if User.objects.filter(email=Email).exists():            
                user = User.objects.get(email = Email)
                if user.is_authenticated:
                    try:
                     student = authenticate(request, username=user.username, password=password)
                     login(request, student)
                    #  messages.success(request,"welcome" + " " +user.username)
                     return redirect('profile_page')
                    except Exception as e:
                        print(e)
                        messages.error(request,"wrong password plz check it.")
                        return render(request, "account/sign_up.html")

                else:
                    messages.error(request,"wrong password plz check it.")
                    return render(request, "account/sign_up.html")
            else:
                messages.error(request,"User Does Not Exits")
                return render(request,"account/sign_up.html")
        else:
            messages.error(request,"confirm password does not match")
            return render(request, "account/sign_up.html")
    else:
        return render(request, "account/sign_up.html")


######### user profile page
@login_required
def User_Profile(request):
    if request.user.is_authenticated:          
        if request.method=='POST':
            form = EditUserProfile(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('profile_page')
            if StudentSocialMedia:                                                                  
                facebook = request.POST.get('facebook')
                instagram = request.POST.get('instagram')
                twitter = request.POST.get('twitter')
                github = request.POST.get('github')
                snapchat = request.POST.get('snapchat')
                data = StudentSocialMedia.objects.create(student = request.user, facebook=facebook, instagram=instagram, twitter=twitter, github=github, snapchat=snapchat)
                data.save()
                return redirect('profile_page')   
            if StudentStories:
                student = request.user.username
                image = request.FILES['student_story']
                title = request.POST.get('student_story_title')
                highlight = request.POST.get('highlight_story')
                object = StudentStories.objects.create(student=student, img=image, title=title)
                object.save()
                return redirect('profile_page') 
            return render(request, "common/profile.html" ,{'name':request.user,'form':form})
        else:
            
            # if StudentSocialMedia.objects.filter(student=request.user).all():               
                 obj = StudentSocialMedia.objects.filter(student=request.user).all()
                 form = EditUserProfile(instance=request.user)            
                 story = StudentStories.objects.filter(student= request.user.username).all()               

                 context = {}
                 context['name'] = request.user
                 context['form'] = form
                 context['media'] = obj
                 context['notification'] = StudentNotification.objects.all()
                 context['story'] = story
                 return render(request, "common/profile.html" ,context)
            # else:
            #     form = EditUserProfile(instance=request.user)
            #     return render(request, "common/profile.html" ,{'name':request.user,'form':form})
    else:
        return render(request, "common/profile.html")
         
######### old user sign up page 
def SignUpView(request):
    abcid = random.randint(100000,999999)
    if request.method == 'POST':
        username = request.POST['user']
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpasword = request.POST.get('confirm_password')
        # name = (firstname)
        if password==confirmpasword:
            if User.objects.filter(email=email).exists():
                messages.error(request,"Email Already Exits Go to Login Page")                
                
                return render(request,"account/login.html")
            else:
                try:
                        student = User.objects.create_user(username=username, email=email, password=password, first_name=firstname, last_name=lastname)
                        student.save()
                        subject = 'Hello from Django'
                        
                        message = f'This is a test email sent from Django. and otp is {abcid}'
                        # recipient_list = ['bajpaisaurya972@gmail.com']  # Replace with the recipient's email addresses
                        send_mail('Welcome To Svm Collage', message, settings.EMAIL_HOST_USER,[email],fail_silently=False)
                        messages.success(request,"The Email is also send this user")
                        login(request,student)
                        return redirect('profile_page')
                except Exception as e:
                    print(e)        
                messages.success(request,"Welcome You in Svm Collage")
                return render(request,"account/login.html")
                
        else:
            messages.error(request,"Your Password and Confirm password does not match")
            return render(request,"account/login.html",{'rand':abcid})     
    else:
        form = ContactForm()
        return render(request,"account/login.html",{'form':form})     


#######  old user change password
class ChangePassword(PasswordChangeView):
    # form_class = PasswordChangeForm
    form_class = PasswordReset
    template_name = "account/change_password.html"
    success_url = reverse_lazy('signup')

##### user log out
def LogoutView(request):    
    logout(request)
    return redirect('login_page')


###notification
def NotificationView(request,slug):
    obj = StudentNotification.objects.get(slug = slug)
    return render(request,"common/notification.html",{'context':obj})


##### Home page
def HomePageView(request):
    return render(request, "dashboard/home.html")



           
    



      









