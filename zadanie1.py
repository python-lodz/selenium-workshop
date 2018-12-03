import unittest

from selenium import webdriver


class WorkshopTests(unittest.TestCase):
    """
    URL: 

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
        pass


if __name__ == "__main__":
    unittest.main()
