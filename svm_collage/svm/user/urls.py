from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from svm.views import *
from user.views import *
from django.contrib.auth import views as auth_view
from django.contrib.auth.views import PasswordResetView,PasswordResetCompleteView,PasswordResetDoneView,PasswordResetCompleteView,PasswordResetConfirmView

urlpatterns = [
    path('login/',LoginView, name='login_page'),
    path('sign-up/',SignUpView, name='sign_up'),
    path('password-reset/', auth_view.PasswordResetForm),
    path('captcha/',include('captcha.urls')),
    path('change-password/',ChangePassword.as_view(),name='cangepassword'),
    path('reset-password/', PasswordResetView.as_view(template_name = "account/password_reset.html"), name='reset'),
    path('reset-password-done/',PasswordResetDoneView.as_view(template_name = "account/password_reset_done.html")),
    path('reset-password-complete/',PasswordResetCompleteView.as_view(template_name = "account/password_reset_complete.html")),
    path('reset-password-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name = "account/password_reset_confirm.html")),
    path('profile-page/',User_Profile, name='profile_page'),
    path('log-out-account/',LogoutView, name='logout_page'),
    path('svm-notifications/<slug:slug>/',NotificationView, name='svmnotifications'),
    path('',HomePageView, name="homepage")

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
