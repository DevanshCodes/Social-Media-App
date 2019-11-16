from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('',include('django.contrib.auth.urls')),
    path('logout/',views.logout_view,name='logout'),
    path('profile/',views.profile,name='profile')
   # path('LoginIndex/',views.IndexLogIn,name='LoginIndex')
]