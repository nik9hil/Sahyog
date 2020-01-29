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

def firstaid(request):
	status = False
	firstaid = database.child('first-aid').shallow().get().val()
	firstaidList = []
	for i in firstaid:
		firstaidList.append(i)
	firstaid = request.POST.get('firstaid')
	urllist = []
	if firstaid in firstaidList:
		searchquery = database.child('first-aid').child(firstaid).shallow().get().val()
		for i in searchquery:
			urllist.append(i)
		print(urllist)
		newlist = []
		for i in urllist:
			search = database.child('first-aid').child(firstaid).child(i).get().val()
			newlist.append(search)
		print(newlist)
		status = True
	else:
		print('do nothing')
	context = {
		'videos' : newlist,
		'status' : status
	}
	return render(request,'firstaid/firstaid.html',context)