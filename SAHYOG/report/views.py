from django.shortcuts import render, redirect
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

def report(request):
        idtoken = request.session['uid']
        a = authenticate.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        mailid = a['email']
        a = a['localId']
        allusers = database.child('users').shallow().get().val()
        complaint_list=[]
        #print(allusers)
        if allusers != None:
            users = []
            for i in allusers:
                if i != a:
                    users.append(i)
            user_complaints = []
            complaintName = []
            animal = []
            address = []
            description = []
            for i in users:
                allusercomplaints = database.child('users').child(i).child('complaints').shallow().get().val()
                if allusercomplaints != None:
                    user_complaints.append(allusercomplaints)
                    for j in user_complaints[-1]:
                        print(j)
                        ename = database.child('users').child(i).child('complaints').child(j).child('complaint').get().val()
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
			'email' : mailid,
            'complaint_list' : complaint_list
		}
        return render(request,'report/reports.html',context)
    