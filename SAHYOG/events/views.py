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
	try:
		a = authenticate.get_account_info(request.session['uid'])
		a = a['users'][0]['email']
		context = {
			'email' : a
		}
		return render(request,'events/eventsform.html',context)
	except:
		message = "Oops! User has been logged out. Please log in again."
		context = {
			'message' : message
		}
		return render(request,'authentication/login.html',context)

def eventsubmit(request):
	eventName = request.POST.get('eventName')
	date = request.POST.get('date')
	address = request.POST.get('placeName')
	description = request.POST.get('description')
	startTime = request.POST.get('startTime')
	endTime = request.POST.get('endTime')
	tz = pytz.timezone('Asia/Kolkata')
	time_now = datetime.now(timezone.utc).astimezone(tz)
	millis = int(time.mktime(time_now.timetuple()))
	try:
		idtoken = request.session['uid']
		print(idtoken)
		a = authenticate.get_account_info(idtoken)
		a = a['users']
		a = a[0]
		a = a['localId']

		data = {
			"eventName" : eventName,
			"date" : date,
			"startTime" : startTime,
			"endTime" : endTime,
			"address" : address,
			"description" : description,
		}

		database.child('users').child(a).child('events').child(millis).set(data,idtoken)
		return redirect('events')
	except KeyError:
		message = "Oops! User logged out. Please log in again."
		context = {
			'message':message
		}
		return render(request,'authentication/login.html',context)

def events(request):
	try:
		idtoken = request.session['uid']
		a = authenticate.get_account_info(idtoken)
		a = a['users']
		a = a[0]
		mailid = a['email']
		a = a['localId']
		timestamps = database.child('users').child(a).child('events').shallow().get().val()
		lis_time = []
		event_list = []
		all_events_list = []
		if timestamps != None:
			for i in timestamps:
				lis_time.append(i)
			lis_time.sort(reverse=True)
			eventName = []
			date = []
			startTime = []
			endTime = []
			address = []
			description = []
			for i in lis_time:
				ename = database.child('users').child(a).child('events').child(i).child('eventName').get().val()
				dat = database.child('users').child(a).child('events').child(i).child('date').get().val()
				stime = database.child('users').child(a).child('events').child(i).child('startTime').get().val()
				etime = database.child('users').child(a).child('events').child(i).child('endTime').get().val()
				addr = database.child('users').child(a).child('events').child(i).child('address').get().val()
				descr = database.child('users').child(a).child('events').child(i).child('description').get().val()
				eventName.append(ename)
				date.append(dat)
				startTime.append(stime)
				endTime.append(etime)
				address.append(addr)
				description.append(descr)
			event_list = zip(eventName,date,startTime,endTime,address,description,lis_time)
		allusers = database.child('users').shallow().get().val()
		if allusers != None:
			users = []
			for i in allusers:
				if i != a:
					users.append(i)
			user_events = []
			user_details = []
			size = 0
			eventName = []
			date = []
			startTime = []
			endTime = []
			address = []
			description = []
			for i in users:
				alluserevents = database.child('users').child(i).child('events').shallow().get().val()
				user_events.append(alluserevents)
				for j in user_events[-1]:
					ename = database.child('users').child(i).child('events').child(j).child('eventName').get().val()
					dat = database.child('users').child(i).child('events').child(j).child('date').get().val()
					stime = database.child('users').child(i).child('events').child(j).child('startTime').get().val()
					etime = database.child('users').child(i).child('events').child(j).child('endTime').get().val()
					addr = database.child('users').child(i).child('events').child(j).child('address').get().val()
					descr = database.child('users').child(i).child('events').child(j).child('description').get().val()
					eventName.append(ename)
					date.append(dat)
					startTime.append(stime)
					endTime.append(etime)
					address.append(addr)
					description.append(descr)

			all_events_list = zip(eventName,date,startTime,endTime,address,description)

		context = {
			'event_list' : event_list,
			'all_events_list' : all_events_list,
			'email' : mailid
		}
		return render(request,'events/events.html',context)
	except:
		message = "Oops! User has been logged out. Please log in again."
		context = {
			'message' : message
		}
		return render(request,'authentication/login.html',context)

def deleteevent(request):
	try:
		time = request.GET.get('z')
		a = authenticate.get_account_info(request.session['uid'])
		a = a['users'][0]['localId']
		database.child('users').child(a).child('events').child(time).remove(request.session['uid'])
		return redirect('events')
	except:
		message = "Oops! User has been logged out. Please log in again."
		context = {
			'message' : message
		}
		return render(request,'authentication/login.html',context)