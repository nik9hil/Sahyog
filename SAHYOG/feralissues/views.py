from django.shortcuts import render, redirect
import time, pytz
from datetime import datetime, timezone
import pyrebase
from django.contrib import auth
#import seaborn as sns

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

def complaint(request):
    try:
        idtoken = request.session['uid']
        a = authenticate.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        mailid = a['email']
        a = a['localId']
        data = database.child('complaints').shallow().get().val()
        complain_list = []
        for i in data:
            complain_list.append(i)
        print("COMPLAINT LIST:",complain_list)
        addr = []
        anim = []
        descr = []
        for i in complain_list:
            addr.append(database.child('complaints').child(i).child('address').get().val())
            anim.append(database.child('complaints').child(i).child('animal').get().val())
            descr.append(database.child('complaints').child(i).child('descrp').get().val())
        complain_list = zip(addr,anim,descr)
        context = {
            'complaint_list' : complain_list,
            'email' : mailid
        }
        return render(request,'feralissues/complaint.html',context)
    except:
        message = "Oops! User logged out."
        context = {
            'message' : message
        }
        return render(request,'authentication/login.html',context)

def complaintform(request):
	try:
		a = authenticate.get_account_info(request.session['uid'])
		a = a['users'][0]['email']
		context = {
			'email' : a
		}
		return render(request,'feralissues/complaintform.html',context)
	except:
		message = "Oops! User has been logged out. Please log in again."
		context = {
			'message' : message
		}
		return render(request,'authentication/login.html',context)

def complaintsubmit(request):
    complaint=request.POST.get('complaint')
    animal = request.POST.get('animal')
    location = request.POST.get('placeName')
    description = request.POST.get('description')
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
			"complaint" : complaint,
			"animal" : animal,
			"address" : location,
			"description" : description,
    	}

        database.child('users').child(a).child('complaints').child(millis).set(data,idtoken)
        return redirect('home')
    except KeyError:
        message = "Oops! User logged out. Please log in again."
        context = {
			'message':message
		}
        return render(request,'authentication/login.html',context)