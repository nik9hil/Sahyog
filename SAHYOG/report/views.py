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
        context = {
            'email' : mailid,
        }
        return render(request,'report/reports.html',context)

class ChartData(APIView):
    def get(self, request, format=None):
        idtoken = request.session['uid']
        a = authenticate.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        mailid = a['email']
        a = a['localId']
        allusers = database.child('users').shallow().get().val()
        if allusers != None:
            users = []
            for i in allusers:
                if i != a:
                    users.append(i)
        data={}
        labels=[]
        for i in users:
            auser = database.child('users').child(i).child('details').child('service').get().val()
            if auser:
                auser = auser.lower()
                if auser in data.keys():
                        data[auser]+=1
                else:
                    data[auser]=1
                    labels.append(auser)
        print(labels)
        print(data)
        datatemp=[]
        for key in data.keys():
            datatemp.append(data[key])
        data = {
            "labels": labels,
            "data": datatemp,
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
        context = {
            'email' : mailid,
        }
        return render(request,'report/reportcomp.html',context)

class Chart(APIView):
    def get(self, request, format=None):
        idtoken = request.session['uid']
        a = authenticate.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        mailid = a['email']
        a = a['localId']
        data={}
        labels=[]
        complaints = database.child('complaints').shallow().get().val()
        for i in complaints:
            auser = database.child('complaints').child(i).child('address').get().val()
            if auser:
                auser = auser.lower()
                if auser in data.keys():
                    data[auser]+=1
                else:
                    data[auser]=1
                    labels.append(auser)
        datatemp=[]
        for key in data.keys():
            datatemp.append(data[key])
        data = {
            "labels": labels,
            "data": datatemp,
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
        context = {
            'email' : mailid,
        }
        return render(request,'report/reportacc.html',context)

class Data(APIView):
    def get(self, request, format=None):
        idtoken = request.session['uid']
        a = authenticate.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        mailid = a['email']
        a = a['localId']
        idtoken = request.session['uid']
        a = authenticate.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        mailid = a['email']
        a = a['localId']
        data={}
        labels=[]
        complaints = database.child('rescue').shallow().get().val()
        for i in complaints:
            auser = database.child('rescue').child(i).child('address').get().val()
            if auser:
                auser = auser.lower()
                if auser in data.keys():
                    data[auser]+=1
                else:
                    data[auser]=1
                    labels.append(auser)
        datatemp=[]
        for key in data.keys():
            datatemp.append(data[key])
        data = {
            "labels": labels,
            "data": datatemp,
        }
        return Response(data)
    
def maps(request):
    print("MARKERS)")
    return render(request,'report/marker.html')