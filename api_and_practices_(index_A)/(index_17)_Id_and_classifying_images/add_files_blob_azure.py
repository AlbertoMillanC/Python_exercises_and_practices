import cv2
import numpy as np
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Conectarse al contenedor de Azure Blob Storage
connect_str = "<AZURE_STORAGE_CONNECTION_STRING>"
container_name = "<NOMBRE_DEL_CONTENEDOR>"
container_client = ContainerClient.from_connection_string(connect_str, container_name)

# Cargamos el clasificador de rostros pre-entrenado
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Iniciamos la captura de video
cap = cv2.VideoCapture(0)

# Inicializamos el contador de rostros y la lista de rostros detectados
face_counter = 0
detected_faces = []

def is_new_face(faces):
    # Compara las caras detectadas con las caras previamente almacenadas
    for face in faces:
        for detected_face in detected_faces:
            if np.allclose(face, detected_face, atol=20):
                return False
    return True

while True:
    # Leemos un fotograma del video
    ret, frame = cap.read()

    # Convertimos el fotograma a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectamos los rostros en el fotograma
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Dibujamos un rectángulo alrededor de cada rostro y asignamos un código
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        face_counter += 1

    # Verificamos si es un rostro nuevo y lo almacenamos en la lista de rostros detectados
    if is_new_face(faces):
        detected_faces.extend(faces)

        # Convertir la imagen a un objeto de memoria
        _, img_encoded = cv2.imencode('.jpg', frame)
        img_bytes = img_encoded.tobytes()

        # Crear un nombre de archivo único para el blob
        blob_name = "rostro_{}.jpg".format(face_counter)

        # Cargar el blob en Azure Storage
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(img_bytes, overwrite=True)

    # Mostramos el fotograma resultante
    cv2.imshow('frame',frame)

    # Salimos del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberamos los recursos al terminar
cap.release()
cv2.destroyAllWindows()