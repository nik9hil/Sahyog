#Import Dependencies
from django.shortcuts import render, redirect
import time, pytz
from datetime import datetime, timezone
import pyrebase
from django.contrib import auth
import requests
from isodate import parse_duration

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

YOUTUBE_DATA_API_KEY='AIzaSyDjQYxufhuDGI9ZfP3Gt2Aa8M_ezh_ssQ4'
search_url = 'https://www.googleapis.com/youtube/v3/search'
video_url = 'https://www.googleapis.com/youtube/v3/videos'


def firstaid(request):
	status = True
	firstaid = database.child('first-aid').shallow().get().val()
	firstaidList = []
	for i in firstaid:
		firstaidList.append(i)
	firstaid = request.POST.get('firstaid')
	urllist = []
	newlist = []
	if firstaid in firstaidList:
		searchquery = database.child('first-aid').child(firstaid).shallow().get().val()
		for i in searchquery:
			urllist.append(i)
		print(urllist)
		for i in urllist:
			video_ids = []
			search = database.child('first-aid').child(firstaid).child(i).get().val()
			search_params = {'part' : 'snippet','q' : search,'key' : 'AIzaSyDbCB6sFqSyK0z0cM1sXvQaETGckhi6wPc','type' : 'video', 'id' : ','.join(video_ids),}
			r = requests.get(search_url, params=search_params)
			results = r.json()['items']
			
			for result in results:
				video_ids.append(result['id']['videoId'])
			for result in results:
				video_data={
					'title':result['snippet']['title'],
					#'id':result['id'],
					'url':'https://www.youtube.com/watch?v={}'.format(result['id']['videoId']),
					
					'thumbnail':result['snippet']['thumbnails']['high']['url']}
				newlist.append(video_data)
		context = {'videos' : newlist, 'status':status}

		print(newlist)
		status = True
	else:
		print('do nothing')
		status = False
	context = {
		'videos' : newlist,
		'status' : status
	}
	return render(request,'firstaid/firstaid.html',context)
