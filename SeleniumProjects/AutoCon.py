from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(2)

        self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(f"{self.username}")
        self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(f"{self.password}")

        time.sleep(2)

        self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div')
        

    
inst = Instagram("Your User Name","Your Password")
inst.signIn()