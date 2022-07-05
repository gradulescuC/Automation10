# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# setam implicit wait in secunde
# selenium va cauta toate elementele timp de x secunde inainte sa dea eroare
chrome.implicitly_wait(1)

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

# elem gasit
chrome.find_element(By.ID, 'first-name').send_keys('Andy')

# id e invalid => NoSuchElementException
chrome.find_element(By.ID, 'last-name123').send_keys('Andy')

# de citit
# https://www.geeksforgeeks.org/implicit-waits-in-selenium-python/