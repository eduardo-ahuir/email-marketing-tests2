"""
Run:
"""
from mailjet_rest import Client
import os
api_key = os.environ['api_key']
api_secret = os.environ['api_secret']
mailjet = Client(auth=(api_key, api_secret))
sujeto=""
sujeto=input("Quien es el sujeto?")
data = {
  'FromEmail': 'eduahuaub@alu.edu.gva.es',
  'FromName': sujeto,
  'Subject': 'Esto es un mail de prueba con una imagen!',
  'Text-part': 'si ves esto la prueba funciona',
  'Html-part': '<h3>Hola</h3><img src=\"https://cdn.discordapp.com/attachments/1087401042511134752/1087747605083201597/dac_logo_4151.png\"> ',
  'Recipients': [ { "Email": "ahuir61@gmail.com" }],

}
result = mailjet.send.create(data=data)
print (result.status_code)
print (result.json())
