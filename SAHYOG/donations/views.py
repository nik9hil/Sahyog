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
def donationsform(request):
	try:
		a = authenticate.get_account_info(request.session['uid'])
		a = a['users'][0]['email']
		allusers = database.child('users').shallow().get().val()
		print("allusers:",allusers)
		if allusers != None:
			users = []
			for i in allusers:
				if i != a:
					users.append(database.child('users').child(i).child('details').child('name').get().val())
			print(users)
		context = {
			'users' : users,
			'email' : a
		}
		return render(request,'donations/donationsform.html',context)
	except:
		message = "Oops! User has been logged out. Please log in again."
		context = {
			'message' : message
		}
		return render(request,'authentication/login.html',context)

def donationsubmit(request):
	name = request.POST.get('name')
	amount = request.POST.get('amount')
	donateto = request.POST.get('donateto')
	message = request.POST.get('message')
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
			"name" : name,
			"amount" : amount,
			"donateto" : donateto,
			"message" : message,
		}

		database.child('users').child(a).child('donations').child(millis).set(data,idtoken)
		return redirect('donations')
	except KeyError:
		message = "Oops! User logged out. Please log in again."
		context = {
			'message':message
		}
		return render(request,'authentication/login.html',context)

def donations(request):
	#dummyURL = database.child('firstAid').shallow().get().val()
	#print(dummyURL)
	try:
		idtoken = request.session['uid']
		a = authenticate.get_account_info(idtoken)
		a = a['users']
		a = a[0]
		mailid = a['email']
		a = a['localId']
		timestamps = database.child('users').child(a).child('donations').shallow().get().val()
		lis_time = []
		donors_list = []
		# all_donors_list = []
		if timestamps != None:
			for i in timestamps:
				lis_time.append(i)
			lis_time.sort(reverse=True)
			print(lis_time)
			name = []
			amount = []
			donateto = []
			message = []
			for i in lis_time:
				try:
					ename = database.child('users').child(a).child('donations').child(i).child('name').get().val()
					eamount = database.child('users').child(a).child('donations').child(i).child('amount').get().val()
					edonateto = database.child('users').child(a).child('donations').child(i).child('donateto').get().val()
					emessage = database.child('users').child(a).child('donations').child(i).child('message').get().val()
					name.append(ename)
					date.append(eamount)
					donateto.append(edonateto)
					message.append(emessage)
				except:
					print("Couldn't fetch the shallow tree")
			donors_list = zip(name,amount,donateto,message,lis_time)
			print(donors_list)
		context = {
			'donors_list' : donors_list,
			# 'all_donors_list' : all_donors_list,
			'email' : mailid
		}
		return render(request,'donations/donations.html',context)
	except:
		message = "Oops! User has been logged out. Please log in again."
		context = {
			'message' : message
		}
		return render(request,'authentication/login.html',context)