# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

sleep(3)

# maximizam fereastra
chrome.maximize_window()

sleep(3)

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/')

sleep(3)

# selector by Link Text
chrome.find_element(By.LINK_TEXT, 'Autocomplete').click() #cu metoda click apasam pe un buton, sau pe un link sau pe orice alt element pe care se poate apasa sa faca ceva

sleep(3)

chrome.quit()