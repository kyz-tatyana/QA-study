import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service('C:/Test/chromedriver.exe')
driver = webdriver.Chrome(service=s)
#OpenSite
driver.get("https://qa.neapro.site/login")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input"). send_keys("kuznetsovatata1984@gmail.com")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input"). send_keys("Tania_1984")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(5)
#Fill Passport
driver.find_element(By.CSS_SELECTOR, ".form:nth-child(2) .document-tile:nth-child(1) > .document-name").click()
driver.find_element(By.ID, "surname"). clear()
driver.find_element(By.ID, "surname"). send_keys("Смирнов")
driver.find_element(By.ID, "name"). clear()
driver.find_element(By.ID, "name"). send_keys("Сергей")
driver.find_element(By.ID, "patronymic"). clear()
driver.find_element(By.ID, "patronymic"). send_keys("Алексеевич")
driver.find_element(By.ID, "passportSeries").clear()
driver.find_element(By.ID, "passportSeries").send_keys("1111")
driver.find_element(By.CSS_SELECTOR, "#birthday > div > i.mx-icon-calendar > svg").click()
driver.find_element(By.CSS_SELECTOR, "#birthday > div > input").send_keys("02.02.1987")
driver.find_element(By.CSS_SELECTOR, "#passportNumber").click()
driver.find_element(By.CSS_SELECTOR, "#passportNumber").clear()
driver.find_element(By.CSS_SELECTOR, "#passportNumber").send_keys("777777")
driver.find_element(By.CSS_SELECTOR, "#dateOfIssue > div > i.mx-icon-calendar > svg").click()
driver.find_element(By.CSS_SELECTOR, "#dateOfIssue > div > input").send_keys("07.07.2007")
driver.find_element(By.CSS_SELECTOR, "#passportNumber").click()
driver.find_element(By.CSS_SELECTOR, "#code").clear()
driver.find_element(By.CSS_SELECTOR, "#code").send_keys("010701")
driver.find_element(By.CSS_SELECTOR, "#cardId").clear()
driver.find_element(By.CSS_SELECTOR, "#cardId").send_keys("10070010070")
driver.find_element(By.CSS_SELECTOR, "#issued").clear()
driver.find_element(By.CSS_SELECTOR, "#issued").send_keys("УВД г.Нижнего Новгорода")
driver.find_element(By.XPATH, "//*[@id='address']/div/div/input").send_keys(Keys.CONTROL+'A')
driver.find_element(By.XPATH, "//*[@id='address']/div/div/input").send_keys(Keys.BACK_SPACE)
driver.find_element(By.XPATH, "//*[@id='address']/div/div/input").send_keys("г Нижний Новгород, ул Адмирала Макарова, д 3")
driver.find_element(By.XPATH, "//*[@id='address']/div/div/input").click()
driver.find_element(By.CSS_SELECTOR, "#phone").clear()
driver.find_element(By.CSS_SELECTOR, "#phone").send_keys("9109101100")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".upload-widget > input").send_keys("C:\\Users\\Tatyana\\Desktop\\Обучение QA\\Passport3.jpg")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".fill").click()