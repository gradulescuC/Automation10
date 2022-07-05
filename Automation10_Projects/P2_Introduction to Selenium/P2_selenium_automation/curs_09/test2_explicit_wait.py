# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# setam implicit wait in secunde
# selenium va cauta toate elementele timp de x secunde inainte sa dea eroare
chrome.implicitly_wait(10)

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

# elem gasit
chrome.find_element(By.ID, 'first-name').send_keys('Andy')
# cauta elementul timp de 10 secunde
last_name = WebDriverWait(chrome, 20).until(EC.presence_of_element_located((By.ID, "last-name")))
last_name.send_keys('S')

# https://www.geeksforgeeks.org/explicit-waits-in-selenium-python/