import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys


class Keyboard(unittest.TestCase):
    USER = (By.ID, 'username')

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)

    def test_select_all(self):
        self.chrome.get("https://the-internet.herokuapp.com/login")
        user = self.chrome.find_element(*self.USER)
        user.send_keys('Andy')
        sleep(1)
        user.clear()
        sleep(2)
        user.send_keys('Andy')
        sleep(1)
        user.send_keys(Keys.COMMAND, 'a')
        sleep(1)
        user.send_keys(Keys.BACKSPACE)
        sleep(2)

    def tearDown(self):
        self.chrome.quit()

# https://the-internet.herokuapp.com/key_presses