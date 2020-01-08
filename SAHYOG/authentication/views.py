#Import Dependencies
from django.shortcuts import render,redirect
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

def login(request):
	return render(request,'authentication/login.html')

def sahyog(request):
	email = request.POST.get('email')
	password = request.POST.get('password')
	try:
		user = authenticate.sign_in_with_email_and_password(email,password)
	except:
		message = "Invalid Credentials. Please try again."
		context = {
			'message' : message
		}
		return render(request,"authentication/login.html",context)
	session_id = user['idToken']
	request.session['uid'] = str(session_id)
	return render(request,'home/home.html',{'email':email})

def logout(request):
	auth.logout(request)
	return render(request,'authentication/login.html')