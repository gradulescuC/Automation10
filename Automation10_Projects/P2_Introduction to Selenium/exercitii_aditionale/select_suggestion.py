from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()
chrome.get('https://www.phptravels.net/')
list_elements = chrome.find_elements(By.XPATH,"//span[@class='select2-selection__arrow']")
list_elements[0].click()
sleep(4)
chrome.find_element(By.XPATH,"//input[@class='select2-search__field']").send_keys("Bucharest")
sleep(6)
chrome.find_element(By.XPATH,"//ul[@id='select2-hotels_city-results']/li/i").click()
sleep(2)
chrome.find_element(By.ID,"checkin").click()
sleep(2)

