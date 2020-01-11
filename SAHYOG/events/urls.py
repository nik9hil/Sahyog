#Import Dependencies
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	#/ /
	path(r'eventsform/',views.eventsform,name='eventsform'),
	path(r'eventsubmit/',views.eventsubmit,name='eventsubmit'),
	path(r'events/',views.events,name='events'),
	path(r'deleteevent/',views.deleteevent,name='deleteevent'),
]