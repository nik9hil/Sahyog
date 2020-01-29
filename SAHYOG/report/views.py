from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import pyrebase
from django.contrib import auth
from django.views.generic import View
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

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

class HomePageView(View):
    def get(self, request, *args, **kwargs):
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

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        idtoken = request.session['uid']
        a = authenticate.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        mailid = a['email']
        a = a['localId']
        data={"Dadar":0,"Byculla":0,"Kalyan":0,"Vidyavihar":0,"Ghatkopar":0,"Kurla":0,"Thane":0,"Vikhroli":0,"Andheri":0}
        allusers = database.child('users').shallow().get().val()
        if allusers != None:
            users = []
            for i in allusers:
                if i != a:
                    users.append(i)
        for i in users:
            auser = database.child('users').child(i).child('details').child('organisation').shallow().get().val()
            if auser!= None and auser=="NGO":
                fuser = database.child('users').child(i).child('details').child('service').shallow().get().val()
                if fuser!=None:
                    data[fuser]+=1

        data = {
            "labels": ["Kalyan","Kurla", "Vidyavihar","Ghatkopar","Vikhroli","Byculla","Dadar","Thane","Andheri"],
            "data": [data["Kalyan"], data["Kurla"], data["Vidyavihar"], data["Ghatkopar"], data["Vikhroli"], data["Byculla"], data["Dadar"],data["Thane"],data["Andheri"]],
        }
        return Response(data)

#===========================================================================

class HomePage(View):
    def get(self, request, *args, **kwargs):
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
        return render(request,'report/reportcomp.html',context)

class Chart(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        idtoken = request.session['uid']
        a = authenticate.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        mailid = a['email']
        a = a['localId']
        data={"Dadar":0,"Byculla":0,"Kalyan":0,"Vidyavihar":0,"Ghatkopar":0,"Kurla":0,"Thane":0,"Vikhroli":0,"Andheri":0}
        allusers = database.child('users').shallow().get().val()
        if allusers != None:
            users = []
            for i in allusers:
                if i != a:
                    users.append(i)
        for i in users:
            auser = database.child('users').child(i).child('details').child('organisation').shallow().get().val()
            if auser!= None and auser=="NGO":
                fuser = database.child('users').child(i).child('details').child('service').shallow().get().val()
                if fuser!=None:
                    data[fuser]+=1

        data = {
            "labels": ["Kalyan","Kurla", "Vidyavihar","Ghatkopar","Vikhroli","Byculla","Dadar","Thane","Andheri"],
            "data": [data["Kalyan"], data["Kurla"], data["Vidyavihar"], data["Ghatkopar"], data["Vikhroli"], data["Byculla"], data["Dadar"],data["Thane"],data["Andheri"]],
        }
        return Response(data)

#============================================================================================================

class HomeView(View):
    def get(self, request, *args, **kwargs):
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
        return render(request,'report/reportacc.html',context)

class Data(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        idtoken = request.session['uid']
        a = authenticate.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        mailid = a['email']
        a = a['localId']
        data={"Dadar":0,"Byculla":0,"Kalyan":0,"Vidyavihar":0,"Ghatkopar":0,"Kurla":0,"Thane":0,"Vikhroli":0,"Andheri":0}
        allusers = database.child('users').shallow().get().val()
        if allusers != None:
            users = []
            for i in allusers:
                if i != a:
                    users.append(i)
        for i in users:
            auser = database.child('users').child(i).child('details').child('organisation').shallow().get().val()
            if auser!= None and auser=="NGO":
                fuser = database.child('users').child(i).child('details').child('service').shallow().get().val()
                if fuser!=None:
                    data[fuser]+=1

        data = {
            "labels": ["Kalyan","Kurla", "Vidyavihar","Ghatkopar","Vikhroli","Byculla","Dadar","Thane","Andheri"],
            "data": [data["Kalyan"], data["Kurla"], data["Vidyavihar"], data["Ghatkopar"], data["Vikhroli"], data["Byculla"], data["Dadar"],data["Thane"],data["Andheri"]],
        }
        return Response(data)
    