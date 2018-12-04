import unittest

from selenium import webdriver


class WorkshopTests(unittest.TestCase):
    """
    Zrefaktoryzuj zadanie 3 i utwórz Page Objects dla:
    - formularza wyszukiwania (wpisz miejsce, wybierz przedział dat)
    - filtrów przedziału cenowego na stronie wyników
    - filtrów ilości gwiazdek na stronie wyników

    Korzystając z gotowych komponentów, napisz dwa scenariusze (metody) testowe:
    - sprawdzający dostępność obiektów o 3 gwiazdkach w marcu 2018
    - sprawdzający że w weekend 15-16. grudnia na Mahattanie nie ma więcej niż 10 dostępnych ofert w najniższym przedziale cenowym

    Page objects:
    https://selenium-python.readthedocs.io/page-objects.html
    """

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_exercise(self):
        pass


if __name__ == "__main__":
    unittest.main()
