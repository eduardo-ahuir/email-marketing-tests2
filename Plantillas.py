from mailjet_rest import Client
import os

# Ingresar las credenciales de Mailjet
api_key = os.environ['api_key']
api_secret = os.environ['api_secret']

# Configurar el cliente de Mailjet
mailjet = Client(auth=(api_key, api_secret), version='v3.1')

# Definir las variables para la plantilla
name = input("Ingrese El nombre: ")
imagen=input("Ingrese El url de la imagen: ")
paraf1=input("Ingrese El Texto del primer parrafo: ")
Email_Envia="pruebas@electricautomationnetwork.com"
Email_Recibe=input("Ingrese El Correo al cual se enviara el mensaje: ")

# Crear los datos del mensaje
data = {
    'Messages': [
        {
            "From": {
                "Email": Email_Envia,
                "Name": "Prueba"
            },
            "To": [
                {
                    "Email": Email_Recibe,

                }
            ],
            "TemplateID": 4680148,
            "TemplateLanguage": True,
            "Subject": "Pruebas",
            "Variables": {
                "name":name,
                "imagen": imagen,
                "paraf1": paraf1
            }
        }
    ]
}

# Enviar el mensaje
result = mailjet.send.create(data=data)

# Imprimir el código de estado y la respuesta de Mailjet
print(result.status_code)
print(result.json())
