from django.shortcuts import render,redirect
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
def adoption(request):
	# try:
		idtoken = request.session['uid']
		a = authenticate.get_account_info(idtoken)
		a = a['users']
		a = a[0]
		mailid = a['email']
		a = a['localId']
		timestamps = database.child('users').child(a).child('adoption').shallow().get().val()
		lis_time = []
		adoption_list=[]
		if timestamps != None:
			for i in timestamps:
				lis_time.append(i)
			lis_time.sort(reverse=True)
			animal = []
			address = []
			description = []
			for i in lis_time:
				try:
					dat = database.child('users').child(a).child('adoption').child(i).child('animal').get().val()
					addr = database.child('users').child(a).child('details').child('service').get().val()
					descr = database.child('users').child(a).child('adoption').child(i).child('description').get().val()
					animal.append(dat)
					address.append(addr)
					description.append(descr)
				except:
					print("Couldn't fetch the shallow tree")
                #print(complaintName)
				adoption_list = zip(animal,address,description,lis_time)
                #print(complaint_list)
		context = {
            'adoption_list' : adoption_list,
            'email' : mailid
		}
		return render(request,'adoption/adoption.html',context)
	# except:
	# 	message = "Oops! User logged out."
	# 	context = {
 #            'message' : message
	# 	}
	# 	return render(request,'authentication/login.html',context)


def adoptionform(request):
	try:
		a = authenticate.get_account_info(request.session['uid'])
		a = a['users'][0]['email']
		context = {
			'email' : a
		}
		return render(request,'adoption/adoptionform.html',context)
	except:
		message = "Oops! User has been logged out. Please log in again."
		context = {
			'message' : message
		}
		return render(request,'authentication/login.html',context)

def adoptionsubmit(request):
    a_id=request.POST.get('id')
    animal = request.POST.get('animal')
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
			"id" : a_id,
			"animal" : animal,
			"description" : description
    	}
        database.child('users').child(a).child('adoption').child(millis).set(data,idtoken)
        return redirect('adoption')
    except KeyError:
        message = "Oops! User logged out. Please log in again."
        context = {
			'message' : message
		}
        return render(request,'authentication/login.html',context)