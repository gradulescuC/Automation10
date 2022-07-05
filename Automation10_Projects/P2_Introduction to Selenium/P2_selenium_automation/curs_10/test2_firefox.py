from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox(executable_path=GeckoDriverManager().install())

firefox.maximize_window()

firefox.get('https://formy-project.herokuapp.com/form')

first_name = firefox.find_element(By.ID, 'first-name')
first_name.send_keys('Andy')

sleep(3)
firefox.quit()

'''
pt alte browsere
https://pypi.org/project/webdriver-manager/#use-with-firefox
'''