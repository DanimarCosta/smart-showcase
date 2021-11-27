from selenium import webdriver
from time import sleep

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

# Instruções dos bots
bot = Bot()