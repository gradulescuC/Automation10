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

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

# selector by Tag - ia primul tot tp. - e ok doar daca avem tag unic
chrome.find_element(By.TAG_NAME, 'input').send_keys('Test')

sleep(3)

# gasim mai multe si le punem in lista
lista_taguri = chrome.find_elements(By.TAG_NAME, 'input') # am definit o lista care sa stocheze toate elementele de pe site identificabile prin tag-ul de input
lista_taguri[1].send_keys('Test1')
lista_taguri[3].click()
print(len(lista_taguri))

sleep(3)

chrome.quit()