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

chrome.get("https://formy-project.herokuapp.com/form")

sleep(1)

date_picker = chrome.find_element(By.ID,"datepicker")
date_picker.click()
dates_list = chrome.find_elements(By.XPATH,"//table/tbody/tr/td[@class='day'] | //table/tbody/tr/td[@class='today day']")

date_evaluated = chrome.find_element(By.XPATH,"/html/body/div[2]/div[1]/table/thead/tr[2]/th[2]").text

print(f"We are going to extract the day for the 3d of {date_evaluated}")
for i in range(len(dates_list)):
      if dates_list[i].text=='3':
            dates_list[i].click()
            break

print(f"Date entered is: 3rd of {date_evaluated}")

sleep(6)

