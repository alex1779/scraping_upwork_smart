#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 02:51:19 2024

@author: rafa
"""
import undetected_chromedriver as uc

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import codecs




driver = uc.Chrome(headless=True,use_subprocess=False)
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
driver = uc.Chrome(options=options)
# driver.get('https://bet365.com')



# driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

driver.get("https://www.upwork.com/ab/account-security/login?redir=%2Fnx%2Ffind-work%2F")
# sleep(7)
# el = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
# el.click()

el = wait.until(EC.element_to_be_clickable((By.ID, "login_username")))
el.send_keys("alex1779@hotmail.com")

el = wait.until(EC.element_to_be_clickable((By.ID, "login_password_continue")))
el.click()
sleep(3)

el = wait.until(EC.element_to_be_clickable((By.ID, "login_password")))
el.send_keys("FlorTraini*1475")

el = wait.until(EC.element_to_be_clickable((By.ID, "login_control_continue")))
el.click()
sleep(5)
# wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-item-label"))) # we logged in successfully

driver.get('https://www.upwork.com/nx/find-work/')
source_page = driver.page_source
soup = BeautifulSoup(source_page, 'html.parser')
source_text=soup.prettify()
source_text = codecs.decode(source_text, 'unicode-escape')

#SOURCE TEXT *********************************************************************************
with open('Source.txt', 'w') as f:
    f.write(source_text)

driver.get('https://www.upwork.com/nx/find-work/most-recent')
source_page = driver.page_source
soup = BeautifulSoup(source_page, 'html.parser')
source_text=soup.prettify()
source_text = codecs.decode(source_text, 'unicode-escape')

#SOURCE TEXT *********************************************************************************
with open('most-recent.txt', 'w') as f:
    f.write(source_text)



driver.quit()

