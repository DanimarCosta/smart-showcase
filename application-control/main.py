import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(1)
detector = HandDetector(detectionCon=0.8, maxHands=2)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

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

    # Mostra o que esta sendo criado
    cv2.imshow("Image", img)
    cv2.waitKey(1)

while True:
    gesture_detector()