import time
import os
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
s = Service(executable_path='C:\\Users\\SYNDAY\\Desktop\\API_startap\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get("https://internetopros.ru/")
time.sleep(5)

try:
    ODIN_VOPROS = driver.find_element("xpath", "//div[@class='question-hint']")
    print("=============Элемент (ОДИН ВОПРОС) найден============")
except NoSuchElementException:
    print("Элемент (ОДИН ВОПРОС) не найден")










