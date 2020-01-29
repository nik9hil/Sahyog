from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	#/ /
	path(r'report/',views.report,name='report'),
	path(r'complaintform/',views.complaintform,name='complaintform'),
	path(r'complaintsubmit/',views.complaintsubmit,name='complaintsubmit'),
	path(r'complaint/',views.complaint,name='complaint'),
]