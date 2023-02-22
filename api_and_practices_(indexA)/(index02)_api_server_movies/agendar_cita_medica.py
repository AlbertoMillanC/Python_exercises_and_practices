import datetime
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Crea una instancia de las credenciales de la cuenta de servicio de Google
creds = Credentials.from_service_account_file('credentials.json')

# Construye el cliente de la API de Google Calendar
calendar_service = build('calendar', 'v3', credentials=creds)

# Crea un nuevo evento en el calendario
event = {
  'summary': 'Consulta médica',
  'start': {
    'dateTime': '2022-12-04T15:00:00.000000Z',
    'timeZone': 'America/Mexico_City'
  },
  'end': {
    'dateTime': '2022-12-04T15:30:00.000000Z',
    'timeZone': 'America/Mexico_City'
  }
}
event = calendar_service.events().insert(calendarId='primary', body=event).execute()
print(f'Evento creado: {event.get("htmlLink")}')
