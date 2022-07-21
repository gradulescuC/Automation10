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
#
# # selector by Xpath - atribut=valoare
# chrome.find_element(By.XPATH, '//input[@id="first-name"]').send_keys('test')
# chrome.find_element(By.XPATH, '//input[@id="first-name"]').clear() #  metoda clear sterge informatii din campul input
#
# # selector by Xpath - * toate elementele care resecta regula
# #  * inseamna un inlocuitor pentru toate elementele care respecta regula
# chrome.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('n')

# -----------------------------------------

# # selector by Xpath - navigare in jos - trecem prin fiecare element
# chrome.find_element(By.XPATH, '//div/div/input[@id="first-name"]').send_keys('r')
#
# # selector by Xpath - navigare in jos - skip tags - cautam oriunde sub form un input care sa respecte regula
# # // = orice mostenitor, / = primul mostenitor
# chrome.find_element(By.XPATH, '//form//input[@id="first-name"]').send_keys('e')
#
# # # selector by Xpath - selectare elem din lista - index incepe de la 1
# chrome.find_element(By.XPATH, '(//input[@class="form-control"])[2]').send_keys('i')


# -----------------------------------------
#
# # # selector by Xpath - OR primul gasit dintre variante  ->  | = sau
# s = chrome.find_element(By.XPATH, '//input[@id="first-name"] | //input[@id="last-name"]')
# # # stergem valorile din input
# s.clear()
# sleep(3)
# s.send_keys('Popescu')
# sleep(1)



# -----------------------------------------
# selector by Xpath - in f de textul partial + luam textul de pe el cu proprietatea text
# full_text = chrome.find_element(By.XPATH, '//a[contains(text(), "Autocomplete")]').text

# full_text = chrome.find_element(By.XPATH, '//a[contains(text(), "Submit")]').text
# assert full_text == 'Submit',"Error, text does not match" # verificam daca textul extras din buton este cel pe care il asteptam
# print("The button was found and it contains the proper text")
#
# submit_button = chrome.find_element(By.XPATH, '//a[contains(text(), "Submit")]')
# submit_button.is_enabled() # verificam daca butonul este activat pe site

# label_result = chrome.find_element(By.XPATH,'//label[@for="first-name"]').text
# assert label_result == "First name"

class_element_list = chrome.find_elements(By.XPATH,"//div[@class='col-sm-offset-2']")
print(class_element_list)
class_element_list[0]

# date_picker = chrome.find_element(By.ID,"datepicker")
# date_picker.send_keys("07/10/2022")
# date_picker.click()
# sleep(2)
# -----------------------------------------

# # # selector by Xpath - in f de textul vizibil
# chrome.find_element(By.XPATH, '//a[text()="Submit"]').click()
# # -----------------------------------------

'''
x y axis navigation
cu parent in sus
cu / elem_type - ajungem la elementul copil
cu //elem_type - cauta prin toti descendentii
cu parent::elem_type in sus
cu following-sibling::elem_type - urmatorul frate de la acelasi nivel
cu preceding-sibling::elem_type - fratele anterior de la acelasi nivel
//label[text()="First name"]/parent::strong
//label[cheie="valoare"]
Navigarea din parinte in copil se face cu /
Navigarea din copil in parinte sau intre frati se face cu //<selector>::
'''

# -----------------------------------------
# cu ajutorul unei functii cand avem foarte multe elemente de acelasi tip
# si vrem sa parametrizam selectorul
# def formy_input_by_placeholder(placeholder_text, input_value):
#     input = chrome.find_element(By.XPATH, f'//input[@placeholder="{placeholder_text}"]')
#     input.clear()
#     input.send_keys(input_value)


# def formy_input_by_label(label, input_value):
#     my_input = chrome.find_element(By.XPATH, f'//label[text()="{label}"]/parent::strong/parent::div//input')
#     my_input.clear()
#     my_input.send_keys(input_value)
#
# formy_input_by_placeholder('Enter first name', 'Alin')
# formy_input_by_placeholder('Enter last name', 'Popescu')
#
# # formy_input_by_label('Job title', 'Automation Engineer')
#
# sleep(3)
# chrome.quit()

# chrome.find_element(By.XPATH,"//div[@class='form-group']/parent::form/div/div[4]/div[2]/input")

# Daca vreau sa plec de la un element si sa ajung la parintele lui scriu /
# dupa element, apoi cuvantul "parent" si apoi semnele "::", si apoi labelul parintelui
