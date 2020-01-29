import pyrebase
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

allusers = database.child('users').shallow().get().val()
all_events_list = dict()
if allusers != None:
	users = []
	for i in allusers:
		users.append(i)
	user_events = []
	user_details = []
	size = 0
	eventName = []
	description = []
	date = []
	endTime = []
	startTime = []
	all_events = []
	for i in users:
		alluserevents = database.child('users').child(i).child('events').shallow().get().val()
		if alluserevents != None:
			user_events.append(alluserevents)
			for j in user_events[-1]:
				if database.child('users').child(i).child('events').child(j).child('address').get().val() == 'Ghatkopar':
					ename = database.child('users').child(i).child('events').child(j).child('eventName').get().val()
					descr = database.child('users').child(i).child('events').child(j).child('description').get().val()
					dat = database.child('users').child(i).child('events').child(j).child('date').get().val()
					etime = database.child('users').child(i).child('events').child(j).child('endTime').get().val()
					stime = database.child('users').child(i).child('events').child(j).child('startTime').get().val()
					
					all_events_list['eventName'] = ename
					all_events_list['description'] = descr
					all_events_list['date'] = dat
					all_events_list['endTime'] = etime
					all_events_list['startTime'] = stime
					all_events.append(all_events_list)
				else:
					continue
print(all_events)
