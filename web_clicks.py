from selenium import webdriver
from time import sleep

navegador = webdriver.Chrome()
navegador.get("https://smart-showcase.netlify.app/")

sleep(10)

elemento = navegador.find_elements_by_id('tag_ensino')

sleep(3)
elemento.click()

#navegador.refresh()