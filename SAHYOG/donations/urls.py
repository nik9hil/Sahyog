#Import Dependencies
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	#/
	path(r'donationsform/',views.donationsform,name='donationsform'),
	path(r'donationsubmit/',views.donationsubmit,name='donationsubmit'),
	path(r'donations/',views.donations,name='donations'),
]