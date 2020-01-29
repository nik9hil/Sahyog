#Import Dependencies
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    #Home
    path('',include('home.urls')),
    #Authentication
    path('',include('authentication.urls')),
    #Events
    path('',include('events.urls')),
    #Feralissues,
    path('',include('feralissues.urls')),
<<<<<<< HEAD
    #Donations
    path('',include('donations.urls')),
=======
    #FirstAid
    path('',include('firstaid.urls')),
>>>>>>> b64dab1f5e6b3be27b919181df70e0fa5a6f3c5d
]