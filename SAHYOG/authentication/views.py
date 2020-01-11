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
database = firebase.database()
print(database)
def login(request):
	return render(request,'authentication/login.html')

def sahyog(request):
	email = request.POST.get('email')
	password = request.POST.get('password')
	try:
		user = authenticate.sign_in_with_email_and_password(email,password)
	except:
		try:
			if request.session['uid']:
				email = request.session['email']
				context = {
					'email' : email
				}
				return render(request,'home/home.html',context)
		except:
			message = "You are logged out. Log in again."
			context = {
				'message' : message
			}
			return render(request,'authentication/login.html',context)
		message = "Invalid Credentials. Please try again."
		context = {
			'message' : message
		}
		return render(request,"authentication/login.html",context)
	session_id = user['idToken']
	request.session['uid'] = str(session_id)
	request.session['email'] = str(user['email'])
	message = "You are logged in"
	context = {
		'email' : email,
		'message' : message
	}
	return render(request,'home/home.html',context)

def logout(request):
	try:
		del request.session['uid']
	except KeyError:
		pass
	return render(request,'authentication/login.html')

def signup(request):
	return render(request,'authentication/signup.html')

def postsignup(request):
	name = request.POST.get('name')
	regnumber = request.POST.get('regnumber')
	organisation = request.POST.get('organisation')
	service = request.POST.get('service')
	email = request.POST.get('email')
	password = request.POST.get('password')
	try:
		user = authenticate.create_user_with_email_and_password(email,password)
	except:
		message = "Unable to create account. Try again."
		context = {
			'message' : message
		}
		return render(request,'authentication/signup.html',context)
	uid = user['localId']
	message = "Account created successfully."
	success = True
	data = {
		'name':name,
		'email':email,
		'regnumber' : regnumber,
		'organisation' : organisation,
		'service' : service,
		'status':'1'
	}
	context = {
		'message' : message,
		'success' : success
	}
	database.child('users').child(uid).child('details').set(data)
	return render(request,'authentication/login.html',context)