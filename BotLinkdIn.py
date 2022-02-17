from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/Mariya/chromedriver.exe')
driver.get('https://www.linkedin.com')
time.sleep(2)

username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")

username.send_keys('my_username')
password.send_keys('my_password')
time.sleep(2)

submit = driver.find_element_by_xpath("//button[@type='submit']").click()