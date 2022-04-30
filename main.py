import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import warnings
from utils import driver_options, split_multi_link

warnings.filterwarnings("ignore", category=DeprecationWarning) 

url = "https://bitly.com/"
options = driver_options(webdriver)

# send over the link

# collect the response

driver = webdriver.Chrome(executable_path=os.getcwd() + "/chromedriver.exe", options=options)

while True:
    input_url = input('URL to shrink: ')
    links = split_multi_link(input_url)
    for link in links:
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "unAuthShortenForm")))

        input_bar = driver.find_element(By.XPATH, "//*[@id=\"shorten_url\"]")
        submit_button = driver.find_element(By.ID, "shorten_btn")

        input_bar.send_keys(link)
        submit_button.click()

        time.sleep(1)
        result = driver.find_element(By.CLASS_NAME, "short-link").text
        print(f"\nOriginal: {link} -> Shrunk: {result}")
    print("\n")