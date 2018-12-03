import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import Select


class WorkshopTests(unittest.TestCase):
    """
    URL: https://breadcrumbscollector.tech/pl/selenium/01.html

    Wcisnij przyciski z sylabami tytułu popularnej piosenki w odpowiedniej kolejności
    i z rozwijanego menu wybierz język w jakim piosenka jest napisana.

    Podpowiedź:
    Pole wyboru to HTMLowski select. Można zobaczyć jak się nim posługiwać w dokumentacji:
    https://selenium-python.readthedocs.io/navigating.html#filling-in-forms
    """

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_exercise(self):
        # miejsce na Twoje rozwiązanie

        next_url = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        print(f'Nastepny URL: {next_url}')


if __name__ == "__main__":
    unittest.main()
