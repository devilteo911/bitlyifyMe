import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning) 

url = "https://bitly.com/"

# send over the link
input_url = input('Insert the URL: ')

# collect the response
# thing to search: span -> short-link, class -> shorten-input, button shorten_btn
options = webdriver.ChromeOptions()
options.headless = True
options.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
options.add_argument("--log-level=3")
options.add_experimental_option('excludeSwitches', ['enable-logging'])


driver = webdriver.Chrome(executable_path=os.getcwd() + "/chromedriver.exe", options=options)
driver.get(url)

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "unAuthShortenForm")))

input_bar = driver.find_element(By.XPATH, "//*[@id=\"shorten_url\"]")
submit_button = driver.find_element(By.ID, "shorten_btn")

input_bar.send_keys(input_url)
submit_button.click()

time.sleep(1)
result = driver.find_element(By.CLASS_NAME, "short-link").text
print(f"\nResult: {result}")




# show the results