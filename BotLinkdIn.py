from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/graficapc/Documents/Bot LinkedIn/chromedriver.exe')
driver.get('https://www.linkedin.com')
time.sleep(2)

username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")

username.send_keys('session_key')
password.send_keys('session_password')
time.sleep(2)

submit = driver.find_element_by_xpath("//button[@type='submit']").click()


#***************** ADD CONTACTS ***********************


driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page=16")
time.sleep(2)

all_buttons = driver.find_elements_by_tag_name("button")
connect_buttons = [btn for btn in all_buttons if btn.text == "Conectar"]

for btn in connect_buttons:
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(2)
    send = driver.find_element_by_xpath("//button[@aria-label='Enviar agora']")
    driver.execute_script("arguments[0].click();", send)
    close = driver.find_element_by_xpath("//button[@aria-label='Fechar']")
    driver.execute_script("arguments[0].click();", close)
    time.sleep(2)