from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()


chrome.get("https://jules.app/sign-in")
sleep(2)
actual_text = chrome.find_element(By.XPATH, "//*[@id='root']/div/div[2]/form/div/div[3]/button").text
# element = WebDriverWait(chrome, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[2]/form/div/div[3]/button")))
sleep(1)
expected_text = "LOG IN"
sleep(1)
assert actual_text == expected_text, f'INVALID Text: expected {expected_text} but found {actual_text}'

print('TEST PASSED')
