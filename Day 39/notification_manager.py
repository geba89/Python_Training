import requests
from twilio.rest import Client 
import os

class NotificationManager:
    def __init__(self):
        self.sid = 'AC775b092a1170804db07ba67fe6a85488'
        self.token = os.environ.get('TWILIO_TOKEN')
        self.messaging_service_sid = 'MGca6e1b32002184d2d6dbdb078e3d8efd'
        self.tel_number = +48512704484
        self.client = Client(self.sid, self.token)

    def send_notification(self, message_body):     
        message = self.client.messages.create(  
                                messaging_service_sid=self.messaging_service_sid, 
                                body=message_body,      
                                to=self.tel_number
                            )