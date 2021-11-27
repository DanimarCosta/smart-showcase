# Bibliotecas
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from time import sleep
from selenium import webdriver

# Configurações iniciais
cap = cv2.VideoCapture(1)
detector = HandDetector(detectionCon=0.8, maxHands=2)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')

def controle(type):
    # Inicia a captura dos frames
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 2)

    for (x, y, w, h) in faces:
        # Corta a imagem quando detectar e tenta reconhecer o objeto
        cut_img = gray[y:y+h, x:x+w]
        cut_color = img[y:y+h, x:x+w]
    
        # Cria um retangulo com base na posição xy, largura e altura
        cv2.rectangle(img, (x ,y), (x + w, y + h), (0, 255, 0), 5)
        face_xy = [x, y] # Valores das coordenadas do rosto
        cv2.putText(img, 'Pessoa Detectada', (x-50, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

        hand_right_x = 0
        face_xy = [0, 0]

        # Configuração inicial das mãos
        success, img = cap.read()
        hands, img = detector.findHands(img) 
        #hands = detector.findHands(img, draw=False)
        
        # Controle da posição das mãos
        if hands:
                # Hand 1
                hand1 = hands[0]
                lmList1 = hand1["lmList"] 
                bbox1 = hand1["bbox"]
                centerPoint1 = hand1["center"]
                handType1 = hand1["type"]
                fingers1 = detector.fingersUp(hand1)
                hand_right = lmList1[8]

                # Controle da aplicação
                if type == "Ativador":
                        try:
                            pos_real_y = y - hand_right[1]
                            posx = x - hand_right[0]
                            if posx >=-250 and posx <= 250:
                                if pos_real_y >= -100:
                                    return True
                
                        # Caso não consiga encontrar, apenas passa para próxima instrução
                        except:
                            pass

                if type == "Movimento":
                        # Tenta encontrar a distancia entre as mãos e a cabeça
                        posx = x - hand_right[0]
                        pos_real_y = y - hand_right[1]
                        
                        if pos_real_y >= -500 and pos_real_y <=-25:
                            if posx <= 300:
                                sleep(1)
                            if posx <= 70:
                                sleep(0.5)
                            if posx <= 50:
                                return 1024
                        
                        else:
                            pass
    
    # Exibe o resultado do processamento
    #cv2.imshow("Image", img)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        return True

# Pagina no Chrome
class Bot():
    # Inicia a classe
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")

    # Entra no link determinado
    def entrar_link(self, link):
        self.driver.get(link)

    # Click nas tags de identificação    
    def click_tag_ensino(self):
        tag_ensino_html = self.driver.find_element_by_id("tag_ensino").click()
        print("ok")
    
    def click_tag_cursos(self):
        tag_cursos_html = self.driver.find_element_by_id("tag_cursos").click()

    def click_tag_tour(self):
        tag_tour_html = self.driver.find_element_by_id("tag_tour").click()

    def click_tag_maps(self):
        tag_maps_html = self.driver.find_element_by_id("tag_maps").click()
    
    # Clicks nas imagens de redirecionamento
    def click_ensino(self):
        img_ensino = self.driver.find_element_by_id("img_ensino").click()
    
    def click_cursos(self):
        img_cursos = self.driver.find_element_by_id("img_cursos").click()
    
    def click_tour(self):
        img_tour = self.driver.find_element_by_id("img_tour").click()
    
    def click_maps(self):
        img_maps = self.driver.find_element_by_id("img_maps").click()

    # Comando para atualizar a pagina
    def atualizar(self):
        self.driver.refresh()
    
    #Comando para voltar a pagina anterior
    def voltar(self):
        self.driver.back()

# Inicializa a pagina
bot = Bot()
bot.entrar_link("https://smart-showcase.netlify.app/")
sleep(10)
print("Vitrine Iniciada com sucesso, inicializando back-end")

# Controlador da imagem
def controlador():
    contador = 0
    while True:
        # Detecta a interação do usuario
        print("Ascene para começar")
        while True:
            status = controle("Ativador")
            if status == True:
                print("Usuario requisitando interação")
                bot.click_tag_ensino()
                sleep(2)
                contador = 1
                break

        # Detecta o movimento do usuario
        print("Detectando movimento...")
        
        # Ensino
        if contador == 1:
            while True:
                status = controle("Movimento")
                if status == 1024:
                    print("Mover para o lado - Detectado")
                    contador = 2
                    bot.atualizar()
                    sleep(0.5)
                    bot.click_tag_cursos()
                    break

                status = controle("Ativador")
                if status == True:
                    bot.click_ensino()

                    # Comando para voltar de pagina
                    sleep(1)
                    while True:
                        status = controle("Ativador")
                        if status == True:
                            bot.voltar()
                            contador = 1
                            break
                    break
        
        # Cursos
        if contador == 2:
            while True:
                status = controle("Movimento")
                if status == 1024:
                    print("Mover para o lado - Detectado")
                    contador = 3
                    bot.atualizar()
                    sleep(0.5)
                    bot.click_tag_tour()
                    break

                status = controle("Ativador")
                if status == True:
                    bot.click_cursos()

                    # Comando para voltar de pagina
                    sleep(1)
                    while True:
                        status = controle("Ativador")
                        if status == True:
                            bot.voltar()
                            contador = 2
                            break
                    break
        
        # Tour
        if contador == 3:
            while True:
                status = controle("Movimento")
                if status == 1024:
                    print("Mover para o lado - Detectado")
                    contador = 4
                    bot.atualizar()
                    sleep(0.5)
                    bot.click_tag_maps()
                    break

                # Tour
                status = controle("Ativador")
                if status == True:
                    bot.click_tour()

                    # Comando para voltar de pagina
                    sleep(1)
                    while True:
                        status = controle("Ativador")
                        if status == True:
                            bot.voltar()
                            contador = 3
                            break
                    break

        # Maps
        if contador == 4:
            while True:
                status = controle("Movimento")
                if status == 1024:
                    print("Mover para o lado - Detectado")
                    contador = 1
                    bot.atualizar()
                    sleep(0.5)
                    bot.click_tag_ensino()
                    break

                # Tour
                status = controle("Ativador")
                if status == True:
                    bot.click_maps()

                    # Comando para voltar de pagina
                    sleep(1)
                    while True:
                        status = controle("Ativador")
                        if status == True:
                            bot.voltar()
                            contador = 4
                            break
                    break

controlador()