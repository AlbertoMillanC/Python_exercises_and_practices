from pymongo import MongoClient
import cv2
from mtcnn import MTCNN

# Conexión a la base de datos MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['nombre_de_tu_base_de_datos']
collection = db['rostros']

# Iniciamos la captura de video
cap = cv2.VideoCapture(0)

# Creamos un objeto detector MTCNN
detector = MTCNN()

# Inicializamos el contador de rostros
face_counter = 0

while True:
    # Leemos un fotograma del video
    ret, frame = cap.read()

    # Detectamos los rostros en el fotograma
    faces = detector.detect_faces(frame)

    # Dibujamos un rectángulo alrededor de cada rostro y asignamos un código
    for face in faces:
        x, y, w, h = face['box']
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        face_counter += 1
        cv2.putText(frame, str(face_counter), (x, y), cv2.FONT_HERSHEY_SIMPLEX,
            1, (255, 0, 0), 2)    # Guardamos el resultado en la base de datos
        collection.insert_one(
            {'codigo': face_counter, 'x': x, 'y': y, 'w': w, 'h': h})

    # Mostramos el fotograma resultante
    cv2.imshow('frame',frame)

    # Salimos del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cerramos la conexión con la base de datos
client.close()
