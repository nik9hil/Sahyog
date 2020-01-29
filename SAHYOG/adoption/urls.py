#Import Dependencies
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	#/ /
	path(r'adoptionform/',views.adoptionform,name='adoptionform'),
	path(r'adoptionsubmit/',views.adoptionsubmit,name='adoptionsubmit'),
	path(r'adoption/',views.adoption,name='adoption'),
]