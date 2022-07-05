# import unittest
import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Test(TestCase):
    # elementele din pagina
    # in loc sa le scriem de n ori in teste, le trecem aici o sg data
    SUBMIT_BTN = (By.XPATH, '//a[@role="button"]')
    FIRST_NAME_INPUT = (By.XPATH, '//input[@id="first-name"]')
    MIDDLE_NAME_INPUT = (By.XPATH, '//input[@id="middle-name"]')

    # se rulaza inainte de fiecare test si are rolul de a face setupul de chrome inainte de fiecare test
    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://formy-project.herokuapp.com/form')

    # se ruleaza dupa fiecare test si are rolul de a inchide driver-ul de chrome dupa fiecare test
    def tearDown(self):
        self.chrome.quit()

    @unittest.skip
    # # verificam URL
    def test_url(self):
        actual = self.chrome.current_url
        expected = 'https://formy-project.herokuapp.com/form'
        # expected value, actual value, mesaj in caz de fail
        self.assertEqual(expected, actual, 'URL is incorrect')

    @unittest.skip
    # # verificam page title
    def test_page_title(self):
        actual = self.chrome.title # se extrage automat titlul paginii incarcate prin intermediul metodei title
        print(f"Titlul extras al paginii este {actual}")
        expected = 'Formy'
        self.assertEqual(expected, actual, 'Page title is incorrect')

    @unittest.skip
    # verificam text de pe element (buton, mesaj de eroare etc)
    def test_submit_btn_text(self):
        # * tuple unpacking - se ia valoarea din tuple si se da ca argument in functie
        actual = self.chrome.find_element(*self.SUBMIT_BTN).text
        expected = 'Submit'
        self.assertEqual(expected, actual, 'Submit btn text is incorrect')

    @unittest.skip
    # # verificam ca element e vizibil
    def test_elem_visible(self):
        elem = self.chrome.find_element(*self.SUBMIT_BTN)
        self.assertTrue(elem.is_displayed(), 'Submit btn nu e vizibil')

    @unittest.skip
    # # verificam ca element are un atribut asteptat (ex clasa)
    def test_elem_atribute(self):
        actual = self.chrome.find_element(*self.SUBMIT_BTN).get_attribute('class')
        expected = 'btn btn-lg btn-primary'
        self.assertEqual(expected, actual, 'Submit btn href attribute is wrong')

    @unittest.skip
    # verificam ca element nu e prezent
    def test_elem_not_displayed(self):
        # ai zice ca merge asa dar nu
        # middle_name = self.chrome.find_element(*self.MIDDLE_NAME_INPUT)
        # self.assertFalse(middle_name.is_displayed(), 'Mid name e vizibil')
        pass

    # verificam ca element nu e prezent v1
    def test_elem_not_displayed_v1(self):
        # verificam ca lista e goala
        middle_name = self.chrome.find_elements(*self.MIDDLE_NAME_INPUT)
        self.assertTrue(len(middle_name) == 0, 'Mid name e vizibil in mod incorect')

    @unittest.skip
    # # verificam ca element nu e prezent v2
    def test_elem_not_displayed_v2(self):
        # verificam ca apare exceptia NoSuchElementException
        try:
            self.chrome.find_element(*self.MIDDLE_NAME_INPUT)
        except NoSuchElementException:
            print("elementul nu se afla pe pagina, este ok")

    @unittest.skip # @unitest.skip este un decorator care instruieste sistemul sa sara peste testul care urmeaza
    # waits pe url
    def test_url_waits(self):
        self.chrome.find_element(*self.SUBMIT_BTN).click()
        # asteptam ca fostul url sa se schimbe
        print(self.chrome.current_url)
        WebDriverWait(self.chrome, 5).until(EC.url_changes('https://formy-project.herokuapp.com/form'))
        # asteptam ca noul url sa contina
        WebDriverWait(self.chrome, 5).until(EC.url_contains('/thanks'))
        # asteptam ca noul url sa fie exact
        WebDriverWait(self.chrome, 5).until(EC.url_to_be('https://formy-project.herokuapp.com/thanks'))
        # daca in 5 secunde nu ajungem pe url corect putem
        try:
            WebDriverWait(self.chrome, 5).until(EC.url_contains('/thanks'))
        except TimeoutException:
            self.assertTrue(False, 'Am asteptat 5 secunde dar url nu se incarca sau nu e corect')