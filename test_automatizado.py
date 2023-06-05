from time import sleep
from selenium import webdriver;
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()

navegador.get("https://www.americanas.com.br/")
navegador.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/header/div[1]/div[1]/main/div/button/div/p').click()
navegador.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/form/div[1]/input').send_keys('17519255')
navegador.find_element(by=By.XPATH, value='//*[@id="rsyswpsdk"]/div/div[2]/div/div/div/div[1]/form/div[2]/button').click()


sleep(10)

