import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(1)
detector = HandDetector(detectionCon=0.8, maxHands=2)

def hand_detector():
    success, img = cap.read()
    #hands, img = detector.findHands(img)  # Desenha os pontos
    hands = detector.findHands(img, draw=False)  # Não desenha os pontos

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmarks points
        bbox1 = hand1["bbox"]  # Bounding Box info x,y,w,h
        centerPoint1 = hand1["center"]  # center of the hand cx,cy
        handType1 = hand1["type"]  # Hand Type Left or Right
        fingers1 = detector.fingersUp(hand1)

        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmarks points
            bbox2 = hand2["bbox"]  # Bounding Box info x,y,w,h
            centerPoint2 = hand2["center"]  # center of the hand cx,cy
            handType2 = hand2["type"]  # Mostra se a mão e a esquerda ou direita

            fingers2 = detector.fingersUp(hand2)
            # print(fingers1, fingers2)
            length, info, img = detector.findDistance(lmList1[8], lmList2[8], img) # with draw

            # Distância entre as mãos
            hand1_pos_xy = lmList1[8]
            hand2_pos_xy = lmList2[8]
            pos_x = abs(hand1_pos_xy[0] - hand2_pos_xy[0])
            pos_y = abs(hand1_pos_xy[1] - hand2_pos_xy[1])
            
            if pos_y >= 100:
                id_posy = "levantadas"
            
            else:
                id_posy = "abaixadas"

            if pos_x >= 300:
                id_posx = "afastadas"
            
            else:
                id_posx = "juntas"
            
            print(f"Os indicadores estao {id_posx} e {id_posy}")

    cv2.imshow("Image", img)
    cv2.waitKey(1)

while True:
    hand_detector()