"""

cod pentru exemplificare identificare dupa id
Pentru a cauta in browser in modulul de inspect elemente identificabile prin perechea atribut = valoare va trebui sa le scriem
    intre doua paranteze patrate (ex: [id="route"])

id = atribute
route = valoare

Pentru a lucra cu browserul, vom avea nevoie de un driver
        care sa fie ca un fel de legatura cu broswerul
Exista cate un driver pentru majoritatea browserelor mai mari: chrome, opera, firefox, safari etc
In trecut acest driver trebuia descarcat si salvat in PC si incarcat in fisierul de python
        in care voiam sa facem automatizarea
Problema cu aceasta metoda era ca de fiecare data cand se facea update la o noua versiune de
        browser trebuia sa descarcam din nou driverul coresponzator (locul de descarcare pentru chrome: https://chromedriver.chromium.org/downloads)
Recent s-a introdus o noua alternativa de descarcare automata a driverului la runtime (adica in timpul executiei programului)

Exemple de elemente:

<input type="text" class="form-control" id="route" placeholder="Street address 2">


"""

# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install()) # Stocam serviciul de chrome
chrome = webdriver.Chrome(service=s) # definirea unei variabile care va stoca driverul de chrome

# maximizam fereastra
chrome.maximize_window() # este o metoda folosita pentru maximizarea browserului

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form') # metoda get este o metoda prin care putem naviga la un anumit link

# selector by ID
# <input type="text" class="form-control" id="first-name" placeholder="Enter first name">

# METODA 1
try:
    first_name = chrome.find_element(By.ID,"first-names") # metoda find_element este o metoda prin care putem sa cautam un element in codul de html pe baza de diversi identificatori
except:
    print("button was not visible on the website - OK")

name = chrome.find_element(By.ID,"first-name")
name.send_keys('Ala Bala Portocala') # metoda send_keys este o metoda care scrie ceva intr-un camp din browser

sleep(3) # sleep este o metoda prin care putem sa punem pauza codului
            #   cu alte cuvinte instruim sistemul sa astepte 3 secunde inainte sa execute urmatoarea instructiune


# METODA 2
chrome.find_element(By.ID,"first-name").send_keys('Ala Bala Portocala')

sleep(3) # folosim metoda sleep ca sa putem sa instruim sistemul sa astepte putin inainte sa inchida sa mearga mai departe

# chrome.quit() # quit este o metoda care este folosita pentru a inchide browserul