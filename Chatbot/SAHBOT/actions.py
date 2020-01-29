from rasa_core_sdk import Action
import requests
import json


class ActionGetFirstAid(Action):

    def name(self):
        return 'action_get_firstaid'

    def run(self, dispatcher, tracker, domain):
        with open('firstaid.json') as f:
            data = json.load(f)
        lisdata = list(data['first-aid'].keys())
        lis = []
        q = tracker.get_slot('firstcategory')
        status = 0
        print("category:",q)
        for i in range(len(lisdata)):
            temp = lisdata[i].split(' | ')
            if len(temp) == 1: 
                temp = lisdata[i].split('or')
            if len(temp) == 1:
                temp = lisdata[i].split('and')
            for m in range(len(temp)):
                temp[m] = temp[m].lower()
            print("TEMP:",temp)
            if q in temp:
                data = data['first-aid'][lisdata[i]]
                length = len(data)
                for j in range(length):
                    urllink = "url"+str(j+1)
                    response = str(j+1) + "." + data[urllink]
                    dispatcher.utter_message(response)
                    status = 1
                break
        if status == 0:
            response = "Sorry, my system couldn't help you out with " + str(q) + "\nCould you specify more precisely?"
            dispatcher.utter_message(response)
        return []

class ActionGetEvents(Action):

    def name(self):
        return 'action_get_events'

    def run(self, dispatcher, tracker, domain):
        q = tracker.get_slot('places').lower()
        print(q)
        message = 'Haan mai, mujhe sab aata hai, mai bhagwaan hoo'
        dispatcher.utter_message(message)
        return []

class ActionGetAdopt(Action):

    def name(self):
        return 'action_get_adoption'

    def run(self, dispatcher, tracker, domain):
        adoption = tracker.get_slot('adoption').lower()
        animal = tracker.get_slot('animal').lower()
        print(adoption,"-",animal)
        message = 'Haan mai, mujhe sab aata hai, mai bhagwaan hoo'
        dispatcher.utter_message(message)
        return []