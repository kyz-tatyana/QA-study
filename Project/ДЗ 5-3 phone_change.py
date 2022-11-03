import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

#changephone:
from lib2to3.pgen2 import driver
s = Service('C:/Test/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://qa.neapro.site/login")
driver.maximize_window()
driver.find_element(By.XPATH, "/html/body/div/div/div/section/div[2]/div/div/div/form/div[1]/div[1]/div/input"). send_keys("kuznetsovatata1984@gmail.com")
driver.find_element(By.XPATH, "/html/body/div/div/div/section/div[2]/div/div/div/form/div[1]/div[2]/div/input"). send_keys("Tania_1984")
driver.find_element(By.XPATH, "/html/body/div/div/div/section/div[2]/div/div/div/form/div[2]/button").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[1]/div/div[1]/div[2]/a/img").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div/div[2]/ul/li[2]/a/img").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/form/div/div/input").clear()
driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/form/div/div/input").send_keys("9101001001")
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/form/button").click()
driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div/div[2]/div/div/div/div[1]/div[2]/img").click()

