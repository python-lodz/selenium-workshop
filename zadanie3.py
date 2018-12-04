import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class WorkshopTests(unittest.TestCase):
    """
    Korzystając ze strony booking.com, znajdź nocleg
    w Nowym Jorku na 6-11. stycznia 2019 na Manhattanie w najniższej dostępnej półce cenowej.

    https://selenium-python.readthedocs.io/waits.html
    """

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_exercise(self):
        self.driver.get('https://booking.com')


if __name__ == "__main__":
    unittest.main()
