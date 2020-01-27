from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class ActionFirstAid(Action):
	def name(self):
		return 'action_firstaid'

	def run(self,dispatcher,tracker,domain):
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
		print(authenticate)
		database = firebase.database()
		query = database.child('first-aid').shallow().get().val()
		print(query)
		problems = []
		for i in query:
			lis = i.split('|')
			lis = i.split('and')
			lis = i.split('or')
			for j in lis:
				problems.append(j)
		print(problems)
		#Get the user requested query
		q = tracker.get_slot('problem')
		newLis = []
		if q in problems:
			query = database.child('first-aid').child(q).shallow().get().val()
			for j in query:
				newLis.append(j)
			response = "Here is the answer:",newLis
		else:
			response = "Sorry, I am not yet intelligent enough to solve this problem."

		dispatcher.utter_message(response)
		return [SlotSet('problem',q)]