
from django.urls import path
from authapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout'),
    path('contact', views.contact, name='contact'),
    path('join', views.enroll, name='enroll'),
    path('profile', views.profile, name='profile'),
    path('gallery', views.gallery, name='gallery'),
    path('attendance',views.attendance,name="attendance"),
    path('services',views.services,name="services"),
    path('about',views.about,name="about"),
    path('team',views.team,name="team"),
    path('change',views.change_pass,name="change"),
]
