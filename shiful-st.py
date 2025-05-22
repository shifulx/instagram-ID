python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.instagram.com/accounts/emailsignup/")

time.sleep(3)

Fill the form
driver.find_element(By.NAME, 'emailOrPhone').send_keys('testmail1234@mail.com')
driver.find_element(By.NAME, 'fullName').send_keys('Rashidul Hacker')
driver.find_element(By.NAME, 'username').send_keys('rashidul_hacker2025')
driver.find_element(By.NAME, 'password').send_keys('TestPassword123')

time.sleep(1)

Click Sign Up
