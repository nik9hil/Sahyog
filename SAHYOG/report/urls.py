from django.contrib import admin
from django.urls import path
from . import views
from .views import HomePageView, ChartData, HomePage, HomeView, Chart, Data

urlpatterns = [
	#/ /
	path(r'reporttt/',HomePageView.as_view(),name='reporttt'),
	path(r'reportt/',HomePage.as_view(),name='reportt'),
	path(r'reporta/',HomeView.as_view(),name='reporta'),
    path('api/chart/data/', ChartData.as_view()),
	path('api/charts/datas/', Chart.as_view()),
	path('api/charta/dataa/', Data.as_view()),
	path(r'maps/',views.maps,name='maps'),
]