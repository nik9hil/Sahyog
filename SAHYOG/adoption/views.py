from django.shortcuts import render
import time, pytz
from datetime import datetime, timezone
import pyrebase
from django.contrib import auth


config = {
  'apiKey': "AIzaSyALcsnA6kvammHw3qVT67I1bIQUAaMgWk4",
  'authDomain': "sahyog-kjscesih.firebaseapp.com",
  'databaseURL': "https://sahyog-kjscesih.firebaseio.com",
  'projectId': "sahyog-kjscesih",
  'storageBucket': "sahyog-kjscesih.appspot.com",
  'messagingSenderId': "1080732247337",
  'appId': "1:1080732247337:web:254d8dd5184624c4bac338",
  'measurementId': "G-8NZGN3H0TJ"
}
firebase = pyrebase.initialize_app(config)
authenticate = firebase.auth()
database = firebase.database()

# Create your views here.
def adoptionform(request):
    try:
        a = authenticate.get_account_info(request.session['uid'])
        a = a['users'][0]['email']
        context = {
            'email' : a
        }
        return render(request,'adoption/adoptionform.html',context)
    except:
        message = "Oops! User has been logged out. Please log in again."
        context = {
			'message' : message
		}
        return render(request,'authentication/login.html',context)

def adoption(request):
    