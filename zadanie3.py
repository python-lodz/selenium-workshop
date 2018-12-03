import unittest

from selenium import webdriver


class WorkshopTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_exercise(self):
        pass


if __name__ == "__main__":
    unittest.main()
