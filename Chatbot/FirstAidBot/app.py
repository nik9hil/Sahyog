from flask import *
import requests
from flask_cors import CORS
import requests
from twilio.rest import Client
import sys
# Flask constructor takes the name of  
# current module (__name__) as argument. 
app = Flask(__name__)
CORS(app) 

account_sid = 'ACe415f6eab1579b9bce14152e18238a0c'
auth_token = '34dcf373a8c5b73caba18ed692efd54d'
client = Client(account_sid, auth_token)


  
# The route() function of the Flask class is a decorator,  
# which tells the application which URL should call  
# the associated function. 
@app.route('/') 
def hello_world(): 
    return render_template('location.html')

@app.route('/twilio',methods=['POST']) 
def loc(): 
    print("data")
    message=request.form['Body']
    print(message)
    uniqueId=request.form['From']
    payload = {"sender": uniqueId,"message": message }
    payload=json.dumps(payload)
    r = requests.post("http://localhost:5005/webhooks/rest/webhook", payload)
    response=r.text
    print(response)
    resp=json.loads(response)
    try:
        reply=resp[0]['text']
        send_to=+919619399169
        message = client.messages.create(
                                body= reply,
                                from_='whatsapp:+14155238886',
                                to='whatsapp:'+str(send_to)
                            )
        print(message.sid)
    except:
        print("something went wrong")
        print(sys.exc_info()[0])
    #key From, To, Body
    return "OK"

@app.route('/loc',methods=['POST'])
def db():
    data=request.get_json()
    print(data)
    return "location received"

  
# main driver function 
if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.run(debug=True) 