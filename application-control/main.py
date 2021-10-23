import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from time import sleep

# Declara as Variaveis
cap = cv2.VideoCapture(1)
detector = HandDetector(detectionCon=0.8, maxHands=2)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

def ativador():
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 2)

    for (x, y, w, h) in faces:
        # Corta a imagem quando detectar e tenta reconhecer o objeto
        cut_img = gray[y:y+h, x:x+w]
        cut_color = img[y:y+h, x:x+w]
    
        # Cria um retangulo com base na pos xy e na largura e altura
        cv2.rectangle(img, (x ,y), (x + w, y + h), (0, 255, 0), 5)
        face_xy = [x, y] # Valores das coordenadas do rosto
        cv2.putText(img, 'Pessoa Detectada', (x-50, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

        
        # Hands
        hand_right_x = 0
        face_xy = [0, 0]
        success, img = cap.read()
        hands, img = detector.findHands(img)  # Desenha os pontos
        #hands = detector.findHands(img, draw=False)  # Não desenha os pontos
        
        if hands:
                # Hand 1
                hand1 = hands[0]
                lmList1 = hand1["lmList"]  # Lista os 21 pontos
                bbox1 = hand1["bbox"]  # Informação da caixa delimitadora x,y,w,h
                centerPoint1 = hand1["center"]  # centro da mão cx,cy
                handType1 = hand1["type"]  # Tipo de mão esquerda ou direita
                fingers1 = detector.fingersUp(hand1)
                hand_right = lmList1[8]

                try:
                    pos_real_y = y - hand_right[1]
                    if pos_real_y >= 100:
                        return True

                except:
                    pass
    
    # Exibe o resultado do processamento
    #cv2.imshow("Image", img)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        return True
    
    # Exibe o resultado para o usuario
    cv2.imshow("Image", img)

    # Mostra o que esta sendo criado
    if cv2.waitKey(20) & 0xFF == ord('q'):
        return 1024

# Coloca a aplicação em um loop
print("Pronto para iniciar")

# Detecta a interação do usuario
while True:
    status = ativador()

    if status == True:
        print("Iniciado com sucesso")
        break

