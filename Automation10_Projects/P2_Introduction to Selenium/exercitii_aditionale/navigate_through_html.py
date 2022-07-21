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
chrome.get('https://www.phptravels.net/') # metoda get este o metoda prin care putem naviga la un anumit link

# city_search_button = chrome.find_element(By.ID,"select2-hotels_city-container")
# city_search_button.click()
# city_search_button.send_keys("Bucharest")
sleep(4)
# dropdown = chrome.find_element(By.XPATH,"//ul[@id='select2-hotels_city-results']")


#  Metode de cautare a textbox-ului pentru email:
chrome.find_element(By.CSS_SELECTOR,"#exampleInputEmail1")
# chrome.find_element(By.CSS_SELECTOR,".form-control sub_email")
# chrome.find_element(By.XPATH,"//input[@id='exampleInputEmail1']")

# Metode de cautare a butonului de submit:
# [id="email_subscribe"
# By.CLASS_NAME,"theme-btn" (metoda de cautare functionala doar in python)
# BY.XPATH,"//button[@class="theme-btn theme-btn-small submit-btn sub_newsletter waves-effect"]"
# BY.LINK_TEXT,"Subscribe"

# metoda de cautare pe baza de partial link text a linkului flights din meniul hamburger
# By.PARTIAL_LINK_TEXT,"fligh"

# message_text = chrome.find_element(By.XPATH,"//span[@class='font-size-14 pt-1 text-white-50']").text
# expected_message = "Don't worry your information is safe with us"
# assert message_text == expected_message, f"Expected message was \"{expected_message}\" but we got \"{message_text}\""

# Navigarea printre elemente:

# 1. Navigarea catre parinte: //parent::<tag_name>
# 2. Navigarea catre un anumit element copil, dintr-o lista specifica <tag_name>[valoare_index]
# 3. Navigarea catre urmatorul frate: //following-sibling::<tag_name>[index_de_navigat_in_jos] (following = urmatorul, sibling = frate)
# 4. Navigarea catre fratele anterior: //preceding-sibling::<tag_name>[index_de_navigat_in_sus] (preceding = anteriorul, sibling = frate)

# //button[@id="currency"]//parent::div/ul/li[3] -> varianta scurta
# //*[@id="fadein"]/header/div[1]/div/div/div[2]/div/div/div[2]/div/ul/li[3]/a -> varianta lunga

# //button[@id="currency"]//parent::div/ul/li[3]//parent::ul/li[4]
# //button[@id="currency"]//parent::div/ul/li[6]//preceding-sibling::li[4]
# //button[@id="supplier"]//parent::div/ul/li

# chrome.find_element(By.XPATH,"//button[@id='supplier']//parent::div//parent::div/following-sibling::div/div/ul/li[1]/a").click()
# chrome.find_element(By.LINK_TEXT,"Signup").click()
lista_dropdown = chrome.find_elements(By.XPATH,"//div[@class='dropdown']")
lista_dropdown[0].click()
sleep(3)
chrome.find_element(By.XPATH,"//button[@id='languages']//parent::div//parent::div/following-sibling::div/div/button").click()
sleep(3)