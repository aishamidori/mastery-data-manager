from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle

def save_cookies():
    email = "gabriel.v.gagnon@gmail.com"
    password = "e4a4eefee975"

    driver = webdriver.Chrome()
    driver.get("https://accounts.google.com/signin")
    email_phone = driver.find_element_by_xpath("//input[@id='identifierId']")
    email_phone.send_keys(email)
    driver.find_element_by_id("identifierNext").click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']")))
    password = driver.find_element_by_xpath("//input[@name='password']")
    password.send_keys(password)
    driver.find_element_by_id("passwordNext").click()
    time.sleep(5)

    cookies = driver.get_cookies()    

    pickle.dump(cookies, open("cookies.pkl")) 

    return cookies


import requests

with requests.Session() as s:
    with open("cookies.pkl","rb") as fd:
        cookies = pickle.load(fd)
	for cookie in cookies:
	    # You should let a driver manage setting and unsetting the cookie
	    driver.add_cookie(cookie)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer": "https://www.google.com/",
        "Accept-Encoding": "deflate",
        "Accept-Language": "en;q=0.6",
        }

    resp = s.get("https://myaccount.google.com/",headers=headers,cookies=cookies)
    print(resp.url)
