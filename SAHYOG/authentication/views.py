#Import Dependencies
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
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

def home(request):
  try:
    a = authenticate.get_account_info(request.session['uid'])
    a = a['users'][0]['email']
    context = {
      'email' : a
    }
    return render(request,'home/home.html',context)
  except:
    message = "Oops! User logged out. Please log in again."
    context = {
      "message" : message
    }
    return render(request,'authentication/login.html',context)