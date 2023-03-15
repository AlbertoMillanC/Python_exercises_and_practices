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

# Inicializamos el contador de rostros
face_counter = 0

while True:
    # Leemos un fotograma del video
    ret, frame = cap.read()

    # Convertimos el fotograma a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectamos los rostros en el fotograma
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Dibujamos un rectángulo alrededor de cada rostro y asignamos un código
    for (x
