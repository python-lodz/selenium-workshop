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
    # https://www.paste.org/96245 - próba wykonania drag and drop bez sukcesu.
    # Element jest łapany i przeciągany ale nie jest upuszczany
    def test_exercise(self):
            self.driver.get('https://breadcrumbscollector.tech/pl/selenium/2223.html')

            recipe = self.driver.find_element_by_id('recipe').text
        
            while(not recipe in 'Gotowe!'):
                action_chains = ActionChains(self.driver)
                if recipe == 'Gotuj na wolnym ogniu':
                    self.driver.find_element_by_css_selector('#heating-control > label:nth-child(1)').click()
                    recipe = self.driver.find_element_by_id('recipe').text
                    continue
                elif recipe == 'Gotuj na dużym ogniu':
                    self.driver.find_element_by_css_selector('#heating-control > label:nth-child(3)').click()
                    recipe = self.driver.find_element_by_id('recipe').text
                    continue
                elif recipe == 'Wrzuć ziemniaka':
                    action_chains.double_click(self.driver.find_element_by_id('potato')).perform()
                    recipe = self.driver.find_element_by_id('recipe').text
                    continue
                elif recipe == 'Wrzuć marchewkę':
                    action_chains.double_click(self.driver.find_element_by_id('carrot')).perform()
                    recipe = self.driver.find_element_by_id('recipe').text
                    continue
                elif recipe == 'Wrzuć sałatę':
                    action_chains.double_click(self.driver.find_element_by_id('lettuce')).perform()
                    recipe = self.driver.find_element_by_id('recipe').text
                    continue
                elif recipe == 'Wrzuć mięso':
                    action_chains.double_click(self.driver.find_element_by_id('meat')).perform()
                    recipe = self.driver.find_element_by_id('recipe').text
                    continue
                
            assert self.driver.find_element_by_id('recipe').text == 'Gotowe!'


if __name__ == "__main__":
    unittest.main()
