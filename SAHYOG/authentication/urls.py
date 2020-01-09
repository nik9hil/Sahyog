#Import Dependencies
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	#/ /
	path('login/',views.login,name='login'),
	path(r'sahyog/',views.sahyog,name='sahyog'),
	path(r'logout/',views.logout,name='logout'),
	path(r'signup/',views.signup,name='signup'),
	path(r'postsignup/',views.postsignup,name='postsignup'),
]