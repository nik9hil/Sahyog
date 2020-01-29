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
        timestamps = database.child('users').child(a).child('complaints').shallow().get().val()
        lis_time = []
        complaint_list = []
        
        if timestamps != None:
            for i in timestamps:
                lis_time.append(i)
            lis_time.sort(reverse=True)
            complaintName = []
            animal = []
            address = []
            description = []
            for i in lis_time:
                try:
                    ename = database.child('users').child(a).child('complaints').child(i).child('complaint').get().val()
                    dat = database.child('users').child(a).child('complaints').child(i).child('animal').get().val()
                    addr = database.child('users').child(a).child('complaints').child(i).child('address').get().val()
                    descr = database.child('users').child(a).child('complaints').child(i).child('description').get().val()
                    complaintName.append(ename)
                    animal.append(dat)
                    address.append(addr)
                    description.append(descr)
                except:
                    print("Couldn't fetch the shallow tree")
                print(complaintName)
                complaint_list = zip(complaintName,animal,address,description,lis_time)
                #print(complaint_list)
        context = {
            'complaint_list' : complaint_list,
            'email' : mailid
        }
        return render(request,'feralissues/complaint.html',context)
    except:
        message = "Oops! User logged out."
        context = {
            'message' : message
        }
        return render(request,'authentication/login.html',context)

def report(request):
    try:
        idtoken = request.session['uid']
        a = authenticate.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        mailid = a['email']
        a = a['localId']
        timestamps = database.child('users').child(a).child('complaints').shallow().get().val()
        lis_time = []
        complaint_list = []
        allusers = database.child('users').shallow().get().val()
        print(allusers['details'])
        '''if allusers != None:
			users = []
			for i in allusers:
				if i != a and i[details][0][]:
					users.append(i)
			print(users)
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
				alluserevents = database.child('users').child(i).child('complaints').shallow().get().val()
				if alluserevents!= None:
					user_events.append(alluserevents)
					for j in user_events[-1]:
						ename = database.child('users').child(i).child('complaints').child(j).child('eventName').get().val()
						dat = database.child('users').child(i).child('complaints').child(j).child('animal').get().val()
						addr = database.child('users').child(i).child('complaints').child(j).child('address').get().val()
						descr = database.child('users').child(i).child('complaints').child(j).child('description').get().val()
						complaintName.append(ename)
						animal.append(dat)
						address.append(addr)
						description.append(descr)
				else:
					continue	
			complaint_list = zip(complaintName,animal,address,description)
        context = {
			'email' : mailid
		}'''
        return render(request,'feralissues/report.html',context)

    except:
        message = "Oops! User has been logged out. Please log in again."
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