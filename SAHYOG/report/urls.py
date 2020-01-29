from django.contrib import admin
from django.urls import path
from . import views
from .views import HomePageView, ChartData

urlpatterns = [
	#/ /
	path(r'reporttt/',HomePageView.as_view(),name='reporttt'),
    path('api/chart/data/', ChartData.as_view()),

]