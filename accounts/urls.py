from django.urls import path
from .views import register_user, login_user, profile, log_out, recruiter_register, recruiter_login

urlpatterns = [
    path('register_user/', register_user, name='register_page'),
    path('login_user/', login_user, name='login_page'),
    path('logout/', log_out, name='log_out_page'),
    path('profile/', profile, name='profile_page'),
    path('register_hr/', recruiter_register, name='register_page_hr'),
    path('login_hr/', recruiter_login, name='login_page_hr'),
] 