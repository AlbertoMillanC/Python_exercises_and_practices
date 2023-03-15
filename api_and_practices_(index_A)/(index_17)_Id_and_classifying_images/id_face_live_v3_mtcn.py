import cv2
from mtcnn import MTCNN

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
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)
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
