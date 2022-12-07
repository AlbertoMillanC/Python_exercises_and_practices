# Importamos la biblioteca de tiempo de Python
import time

# Importamos el módulo de servidores web de Python
from http.server import HTTPServer, BaseHTTPRequestHandler

# Importamos el módulo json para convertir diccionarios a cadenas json
import json

# Definimos una clase que hereda de BaseHTTPRequestHandler y sobrescribe
# el método do_GET para manejar las solicitudes GET
class TimeAPI(BaseHTTPRequestHandler):
  # Sobrescribimos el método do_GET para manejar las solicitudes GET
  def do_GET(self):
    # Obtenemos el parámetro 'location' de la solicitud
    location = self.parse_qs(self.path[2:])['location'][0]

    # Obtenemos la zona horaria de la ubicación
    # (en este ejemplo asumimos que se conoce de antemano)
    timezone = 'CET'

    # Obtenemos la hora local en esa zona horaria
    local_time = time.strftime('%H:%M:%S', time.localtime(time.time(), timezone))

    # Creamos un diccionario con la hora local y la zona horaria
    response = {
      'time': local_time,
      'timezone': timezone
    }

    # Convertimos el diccionario a una cadena json
    response_json = json.dumps(response)

    # Establecemos el código de estado y la cabecera de la respuesta
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()

    # Devolvemos la respuesta
    self.wfile.write(response_json.encode('utf-8'))

# Creamos un servidor web
server = HTTPServer(('0.0.0.0', 8000), TimeAPI)

# Iniciamos el servidor
server.serve_forever()