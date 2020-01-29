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

data = database.child('users').shallow().get().val()
all_users = []
for i in data:
	all_users.append(i)
if all_users != None:
	users = []
	for i in all_users:
		users.append(i)
	adoptions = []
	adoption = []
	animal = []
	description = []
	all_adoption = []
	adoptionList = dict()
	for i in users:
		adoptions = database.child('users').child(i).child('adoption').shallow().get().val()
		if adoptions != None:
			 adoption.append(adoptions)
			 for j in adoption[-1]:
			 	jaanwar = database.child('users').child(i).child('adoption').child(j).child('animal').get().val()
			 	descr = database.child('users').child(i).child('adoption').child(j).child('description').get().val()
			 	adoptionList['animal'] = jaanwar
			 	adoptionList['description'] = descr
			 	all_adoption.append(adoptionList)
print(all_adoption)
