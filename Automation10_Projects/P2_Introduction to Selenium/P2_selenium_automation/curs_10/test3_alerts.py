import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Alerts(unittest.TestCase):
    ALERT = (By.XPATH, '//button[text()="Click for JS Alert"]')
    CONFIRM = (By.XPATH, '//button[text()="Click for JS Confirm"]')
    PROMPT = (By.XPATH, '//button[text()="Click for JS Prompt"]')

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)
        self.chrome.get("https://the-internet.herokuapp.com/javascript_alerts")

    def test_alert(self):
        self.chrome.find_element(*self.ALERT).click()
        # Switch the control to the Alert window
        obj = self.chrome.switch_to.alert
        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)
        sleep(3)
        # use the accept() method to accept the alert
        obj.accept() # metoda accept reprezinta echivalentul clickului pe butonul "OK" din alerta
        print("Clicked on the OK Button in the Alert Window")

    def tearDown(self) -> None:
        self.chrome.quit()

    @unittest.skip
    def test_confirm_ok(self):
        self.chrome.find_element(*self.CONFIRM).click()
        obj = self.chrome.switch_to.alert
        # Retrieve the message on the Confirm window
        message = obj.text
        print(f"Alert shows following message: {message}" )
        sleep(3)
        # use the accept() method to accept the Confirm
        obj.accept()
        print("Clicked on the OK Button in the Confirm Window")
        sleep(3)

    def test_confirm_cancel(self):
        self.chrome.find_element(*self.CONFIRM).click()
        # Switch the control to the Confirm window
        obj = self.chrome.switch_to.alert
        # Retrieve the message on the Confirm window
        message = obj.text
        print("Confirm shows following message: " + message)
        sleep(3)
        # use the dismiss() method to cancel the Confirm
        obj.dismiss() # metoda dismiss este echivalentul butonului de "Cancel" din alerta
        print("Clicked on the Cancel Button in the Confirm Window")
        sleep(3)

    def test_prompt(self):
        pass
        self.chrome.find_element(*self.PROMPT).click()
        # Switch the control to the Prompt window
        obj = self.chrome.switch_to.alert
        # Retrieve the message on the Prompt window
        message = obj.text
        print("Prompt shows following message: " + message)
        # Enter text into the Prompt using send_keys()
        obj.send_keys('Andy')
        # use the accept() method to accept the Prompt
        obj.accept()
        print("Clicked on the OK Button in the Prompt Window")
        sleep(3)
