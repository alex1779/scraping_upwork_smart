#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 02:28:09 2024

@author: rafa
"""

import pyttsx3
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent
import codecs
import os
import time
from datetime import datetime, timedelta
from docx import Document
import warnings
import sys
from googletrans import Translator
import docx



def main():
    
    warnings.filterwarnings("ignore", category=DeprecationWarning) 
    time.sleep(5)
    options = webdriver.ChromeOptions()
    
    options.add_argument('--headless')
    options.add_argument("--incognito")
    options.add_argument("--nogpu")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280,1280")
    options.add_argument("--no-sandbox")
    options.add_argument("--enable-javascript")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    ua = UserAgent()
    userAgent = ua.random
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": userAgent})
    url2 = 'https://www.upwork.com/nx/find-work/most-recent'
    # url = 'https://www.upwork.com/nx/search/jobs/?from_recent_search=true&q='+words+'&sort=recency'
    driver.get(url2)
    source_page = driver.page_source
    soup = BeautifulSoup(source_page, 'html.parser')
    driver.quit()
    source_text=soup.prettify()
    source_text = codecs.decode(source_text, 'unicode-escape')
        
    #SOURCE TEXT *********************************************************************************
    with open('Source.txt', 'w') as f:
        f.write(source_text)


if __name__ == '__main__':
    main()













