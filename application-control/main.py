import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from time import sleep

# Declara as Variaveis
cap = cv2.VideoCapture(1)
detector = HandDetector(detectionCon=0.8, maxHands=2)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

def hand_distance():
    success, img = cap.read()
    #hands, img = detector.findHands(img)  # Desenha os pontos
    hands = detector.findHands(img, draw=False)  # Não desenha os pontos

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # Lista os 21 pontos
        bbox1 = hand1["bbox"]  # Informação da caixa delimitadora x,y,w,h
        centerPoint1 = hand1["center"]  # centro da mão cx,cy
        handType1 = hand1["type"]  # Tipo de mão esquerda ou direita
        fingers1 = detector.fingersUp(hand1)

        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # Lista os 21 pontos
            bbox2 = hand2["bbox"]  # Informação da caixa delimitadora x,y,w,h
            centerPoint2 = hand2["center"]  # centro da mão cx,cy
            handType2 = hand2["type"]  # Mostra se a mão e a esquerda ou direita

            fingers2 = detector.fingersUp(hand2)
            # print(fingers1, fingers2)
            length, info, img = detector.findDistance(lmList1[8], lmList2[8], img) # Com desenho

            # Define as cordenas dos pontos e define a distancia entre as mãos
            hand1_pos_xy = lmList1[8]
            hand2_pos_xy = lmList2[8]
            pos_x = abs(round(hand1_pos_xy[0] - hand2_pos_xy[0]))
            pos_y = abs(round(hand1_pos_xy[1] - hand2_pos_xy[1]))
            
            # Define a posição das mãos em relação a outra
            coordinates = [pos_x, pos_y]
            return coordinates

    #cv2.imshow("Image", img)
    cv2.waitKey(1)

def gesture_detector():
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

        if handType1 == "Left":
            pass
        
        else:
            # Pos_xy da mão direita
            hand_right = lmList1[8]
            hand_right_x = hand_right[0]
            hand_right_y = hand_right[1]

            # Procura um objeto de referencia (neste caso o rosto)
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
        cv2.putText(img, 'Pessoa', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

    # Exibe o movimento
    if hand_right_x or face_xy == 0:
        movimento_px = abs(hand_right_x - face_xy[0])
        print(movimento_px / 10)
   
    else:
        pass

    # Exibe o resultado para o usuario
    cv2.imshow("Image", img)

    # Mostra o que esta sendo criado
    if cv2.waitKey(20) & 0xFF == ord('q'):
        return 1024

def movimentos():
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 2)

    for (x, y, w, h) in faces:
        # Corta a imagem quando detectar e tenta reconhecer o objeto
        cut_img = gray[y:y+h, x:x+w]
        cut_color = img[y:y+h, x:x+w]
    
        # Cria um retangulo com base na pos xy e na largura e altura
        cv2.rectangle(img, (x ,y), (x + w, y + h), (0, 255, 0), 5)
        face_xy = [x, y] # Valores das coordenadas do rosto
        cv2.putText(img, 'Pessoa Detectada', (x-50, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

        # Detecta sorriso
        smiles = smile_cascade.detectMultiScale(cut_img, 1.1, 20)
        if smiles in smiles:
            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(cut_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
                cv2.putText(img, 'Sorriso', (sx+250, sy+100), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,42), 2)
            
            ativado = True
        
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
                    if ativado == True:
                        posx = x - hand_right[0]
                        print (posx)

                        if posx <= 300:
                            sleep(0.5)
                            if posx <= 50:
                                return True
                    
                except:
                    ativado = False
    
    # Exibe o resultado para o usuario
    cv2.imshow("Image", img)

    # Mostra o que esta sendo criado
    if cv2.waitKey(20) & 0xFF == ord('q'):
        return 1024

# Coloca a aplicação em um loop
def app():
    while True:
        retorno_lógico = movimentos()

        if retorno_lógico == True:
            print("Mover para o lado direito")
            print("")
            print("")
            sleep(1.5)
            print("Teste realizado com sucesso, movimento detectado")
            print("")
            print("")
            break

        # Controla o loop
        if retorno_lógico == 1024:
            break

app()