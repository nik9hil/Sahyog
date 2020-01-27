from rasa_core_sdk import Action
import requests
import json


class ActionGetNewst(Action):

    def name(self):
        return 'action_get_information'

    def run(self, dispatcher, tracker, domain):
        with open('sahyog-kjscesih-export.json') as f:
            data = json.load(f)
        lisdata = list(data['first-aid'].keys())
        lis = []
        q = tracker.get_slot('category')
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
                break
        return []