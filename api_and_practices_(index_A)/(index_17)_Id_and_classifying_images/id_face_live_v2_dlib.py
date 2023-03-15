import dlib
import cv2
import numpy as np

# Cargamos el detector de rostros de dlib
detector = dlib.get_frontal_face_detector()

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
    faces = detector(gray)

    # Dibujamos un rectángulo alrededor de cada rostro y asignamos un código
    for face in faces:
        x, y = face.left(), face.top()
        w, h = face.right() - x, face.bottom() - y
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        face_counter += 1
        cv2.putText(frame, str(face_counter), (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    # Mostramos el fotograma resultante
    cv2.imshow('frame',frame)

    # Salimos del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberamos la captura de video y destruimos todas las ventanas
cap.release()
cv2.destroyAllWindows()