import requests
from flask import Flask
from flask import request
from flask import send_from_directory
from twilio import twiml
import subprocess

app = Flask(__name__)
app.config


@app.route('/sms', methods=['POST','GET'])
def sms():
	number = request.form['From']
	message_body = request.form['Body']
	resp = twiml.Response()
			
	if (message_body.lower() == 'unlock'):
    #execute script to send 1/high to output gpio port to arduino
		subprocess.call('./unlock_door.sh')
		resp.message('Door access granted.')

    #pause for 3 seconds
    for i in range (0,2):
      sleep(1)

    #execute script to send 0/low to output gpio port to arduino
    subprocess.call('./lock_door.sh')
	else:
		resp.message('That day, no one saw anything.')

	return str(resp)

if __name__  == '__main__':
	app.run()

