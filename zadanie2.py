import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains


class WorkshopTests(unittest.TestCase):
    """
    URL: <aby poznać URL, musisz rozwiązać zadanie 1.>


    Drugie zadanie polega na przyrządzeniu posiłku wedle przepisu podanego na ekranie.
    W polu tekstowym o id = recipe będą pojawiać się kolejne kroki.
    Każda pomyłka oznacza porażkę.

    Do dyspozycji masz:
    - ustawianie temperatury za pomocą kontrolki typu radio (reaguje na click())
    - składniki które możesz przeciągać do garnka

    Uwaga - jeżeli z jakiegoś powodu drag-and-drop nie działa, użyj podwójnego kliknięcia na składniku.

    Dokumentacja:
    drag'n'drop: https://selenium-python.readthedocs.io/navigating.html#drag-and-drop
    lokalizowanie elementów: https://selenium-python.readthedocs.io/locating-elements.html
    """

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_exercise(self):
        self.driver.get('Z POPRZEDNIEGO ZADANIA')

        assert self.driver.find_element_by_id('recipe').text == 'Gotowe!'


if __name__ == "__main__":
    unittest.main()
