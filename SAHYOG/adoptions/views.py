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

def adoptions(request):
	dummyURL = database.child('firstAid').shallow().get().val()
	print(dummyURL)
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
			print(lis_time)
			eventName = []
			date = []
			startTime = []
			endTime = []
			address = []
			description = []
			for i in lis_time:
				try:
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
				except:
					print("Couldn't fetch the shallow tree")
			event_list = zip(eventName,date,startTime,endTime,address,description,lis_time)
			print(event_list)
		allusers = database.child('users').shallow().get().val()
		print(allusers)
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
					try:
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
					except:
						print("Could not fetch the shallow tree")

			all_events_list = zip(eventName,date,startTime,endTime,address,description)
		print(all_events_list)
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