"""
Created on Sun June 25 09:02:36 2017

@author: muzinga
"""
from twilio.rest import Client

class Message:
	def __init__(self):
		self.account_sid = "AC59592f7f0fb983ee92bb4d0aacfec1e2"
		self.auth_token = "9bf81090628c3206b39c8648eac91e1a"
		self.client = Client(self.account_sid, self.auth_token)
	
	def sendTexto(self,to,sms):
		message = self.client.api.account.messages.create(to=to,from_="+33644601266",body=sms)
