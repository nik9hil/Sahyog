#Import Dependencies
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	#/ /
	path(r'firstaid/',views.firstaid,name='firstaid'),
]