# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
sleep(1)

# maximizam fereastra
chrome.maximize_window()
sleep(1)

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/')

sleep(2)

# selector by Partial Link Text
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Enab').click()
# chrome.find_element(By.LINK_TEXT, 'Enabled and disabled elements').click() -> Acelasi lucru, varianta mai lunga

sleep(3)

chrome.quit()