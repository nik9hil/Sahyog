#Import Dependencies
from django.shortcuts import render, redirect
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
def eventsform(request):
	return render(request,'events/eventsform.html')

def eventsubmit(request):
	eventName = request.POST.get('eventName')
	date = request.POST.get('date')
	placeName = request.POST.get('placeName')
	description = request.POST.get('description')

	tz = pytz.timezone('Asia/Kolkata')
	time_now = datetime.now(timezone.utc).astimezone(tz)
	millis = int(time.mktime(time_now.timetuple()))
	try:
		idtoken = request.session['uid']
		a = authenticate.get_account_info(idtoken)
		a = a['users']
		a = a[0]
		a = a['localId']
		data = {
			"eventName" : eventName,
			"date" : date,
			"placeName" : placeName,
			"description" : description
		}

		database.child('users').child(a).child('events').child(millis).set(data,idtoken)
		email = database.child('users').child(a).child('details').child('name').get(idtoken).val()
		context = {
			'email' : email
		}
		return render(request,'home/home.html',context)
	except KeyError:
		message = "Oops! User logged out. Please log in again."
		context = {
			'message':message
		}
		return render(request,'authentication/login.html',context)