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
        self.driver.get('https://booking.com')

    def tearDown(self):
        self.driver.quit()

    def test_exercise(self):
        self.driver.find_element_by_id('ss').send_keys('Nowy Jork Manhattan')  
        self.driver.find_element_by_class_name('sb-date-field__icon').click()
        self.driver.find_element_by_css_selector('#frm > div.xp__fieldset.accommodation > div.xp__dates.xp__group > div.xp-calendar > div > div > div.bui-calendar__content > div:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(7)').click()
        self.driver.find_element_by_css_selector('#frm > div.xp__fieldset.accommodation > div.xp__dates.xp__group > div.xp-calendar > div > div > div.bui-calendar__content > div:nth-child(2) > table > tbody > tr:nth-child(3) > td:nth-child(5)').click()
        self.driver.find_element_by_class_name('sb-searchbox__button').click()
        self.driver.find_element_by_partial_link_text('od najniższej').click() #przy założeniu strony w wersji polskojęzycznej
        
        print('Found accommodation: ' + WebDriverWait(self.driver, 9).until(expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, '#hotellist_inner > div:nth-child(1) > div.sr_item_content.sr_item_content_slider_wrapper > div.sr_property_block_main_row > div.sr_item_main_block > h3 > a > span.sr-hotel__name'))).text)


if __name__ == "__main__":
    unittest.main()
