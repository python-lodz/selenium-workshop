import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class WorkshopTests(unittest.TestCase):
    """
    Zrefaktoryzuj zadanie 3 i utwórz Page Objects dla:
    - formularza wyszukiwania (wpisz miejsce, wybierz przedział dat)
    - filtrów przedziału cenowego na stronie wyników
    - filtrów ilości gwiazdek na stronie wyników

    Korzystając z gotowych komponentów, napisz dwa scenariusze (metody) testowe:
    - sprawdzający dostępność obiektów o 3 gwiazdkach w marcu 2019
    - sprawdzający że w weekend 15-16. grudnia na Manhattanie nie ma więcej niż 10 dostępnych ofert w najniższym przedziale cenowym

    Page objects:
    https://selenium-python.readthedocs.io/page-objects.html
    """
    _InputField = 'ss'
    _ValueToSearch = 'Manhattan, Nowy Jork'
    _DateField = 'sb-date-field__icon'
    _DayInCalendarFrom = '#frm > div.xp__fieldset.accommodation > div.xp__dates.xp__group > div.xp-calendar > div > div > div.bui-calendar__content > div:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(5)'
    _DayInCalendarTo = '#frm > div.xp__fieldset.accommodation > div.xp__dates.xp__group > div.xp-calendar > div > div > div.bui-calendar__content > div:nth-child(2) > table > tbody > tr:nth-child(6) > td:nth-child(7)'
    _SearchButton = 'sb-searchbox__button'
    _PartNameLinkToSortByPrice = 'od najniższej'
    _CheapestAccomodation = '#hotellist_inner > div:nth-child(1) > div.sr_item_content.sr_item_content_slider_wrapper > div.sr_property_block_main_row > div.sr_item_main_block > h3 > a > span.sr-hotel__name'
    #_FilterByPriceInCheckBox = '0 zł - '
    _FilterByLowestPrice = '#filter_price > div.filteroptions > a:nth-child(1)'
    _FilterByStarInCheckBox = '3 gwiazdki'
    _MonthInCalendar = 'marzec 2019'
    _PlaceDateInCalendar = '#frm > div.xp__fieldset.accommodation > div.xp__dates.xp__group > div.xp-calendar > div > div > div.bui-calendar__content > div:nth-child(2) > div'
    _ArrowToNextMonthInCalendar = '#frm > div.xp__fieldset.accommodation > div.xp__dates.xp__group > div.xp-calendar > div > div > div.bui-calendar__control.bui-calendar__control--next > svg'
    _15December = '#frm > div.xp__fieldset.accommodation > div.xp__dates.xp__group > div.xp-calendar > div > div > div.bui-calendar__content > div:nth-child(1) > table > tbody > tr:nth-child(4) > td:nth-child(6)'
    _16December = '#frm > div.xp__fieldset.accommodation > div.xp__dates.xp__group > div.xp-calendar > div > div > div.bui-calendar__content > div:nth-child(1) > table > tbody > tr:nth-child(4) > td:nth-child(7)'
    _ObjectsOnSearchList = 'sr_item_main_block'
    _check1 = 'Dostępność obiektów o 3 gwiazdkach w marcu 2019: '
    _check2 = 'W weekend 15-16. grudnia na Manhattanie nie ma więcej niż 10 dostępnych ofert w najniższym przedziale cenowym: '
    
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_exercise(self):  
        #sprawdzający dostępność obiektów o 3 gwiazdkach w marcu 2019  
        self.CheckTheAvailabilityOf_3_StarFacilitiesInMarch2019()

        #sprawdzający że w weekend 15-16. grudnia na Manhattanie nie ma więcej niż 10 dostępnych ofert w najniższym przedziale cenowym
        self.ThereNoMoreThan_10_AvailableOffersInTheLowestPriceRangeIn15And16December()

    def tearDown(self):
        self.driver.quit()

    def inputValueToSearch(self, _InputField, _ValueToSearch):
        self.driver.find_element_by_id(_InputField).send_keys(_ValueToSearch)

    def clickOnCalendar(self, _DateField):
        self.driver.find_element_by_class_name(_DateField).click()

    def chooseDateInCalendar(self, _DayInCalendarFrom, _DayInCalendarTo):
        self.driver.find_element_by_css_selector(_DayInCalendarFrom).click()
        self.driver.find_element_by_css_selector(_DayInCalendarTo).click()

    def clickSearchButton(self, _SearchButton):
        self.driver.find_element_by_class_name(_SearchButton).click()

    def sortResultsOnPage(self, _PartNameLinkToSortByPrice):
        self.driver.find_element_by_partial_link_text(_PartNameLinkToSortByPrice).click() #przy założeniu strony w wersji polskojęzycznej

    def chooseCheapestPlace(self, _CheapestAccomodation):
        print(WebDriverWait(self.driver, 9).until(expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, _CheapestAccomodation))).text)

    def filterByPrice(self, _FilterByLowestPrice):
        self.driver.find_element_by_css_selector(_FilterByLowestPrice).click()

    def filterByStar(self, _FilterByStarInCheckBox):
        self.driver.find_element_by_partial_link_text(_FilterByStarInCheckBox).click()
    
    def findMonthInCalendar(self, _MonthInCalendar, _PlaceDateInCalendar, _ArrowToNextMonthInCalendar):
        while not _MonthInCalendar in self.driver.find_element_by_css_selector(_PlaceDateInCalendar).text:
            self.driver.find_element_by_css_selector(_ArrowToNextMonthInCalendar).click()
        return

    def countFoundAccomodation(self, text, _ObjectsOnSearchList, _ValueToSearch):
        counter = 0
        foundAccommodations = str(self.driver.find_elements_by_class_name(_ObjectsOnSearchList))

        for item in foundAccommodations:
            if _ValueToSearch in item: 
                counter += 1
            else:
                continue
        print(str(text + ': {}').format(counter < 10)) 
    
    def ThereNoMoreThan_10_AvailableOffersInTheLowestPriceRangeIn15And16December(self):
        self.driver.get('https://booking.com')  
        self.inputValueToSearch(self._InputField, self._ValueToSearch)
        self.clickOnCalendar(self._DateField)
        self.chooseDateInCalendar(self._15December, self._16December)
        self.clickSearchButton(self._SearchButton)
        self.filterByPrice(self._FilterByLowestPrice)
        self.countFoundAccomodation(self._check2, self._ObjectsOnSearchList, self._ValueToSearch)
        
    def CheckTheAvailabilityOf_3_StarFacilitiesInMarch2019(self):
        self.driver.get('https://booking.com')  
        self.inputValueToSearch(self._InputField, self._ValueToSearch)
        self.clickOnCalendar(self._DateField)
        self.findMonthInCalendar(self._MonthInCalendar, self._PlaceDateInCalendar, self._ArrowToNextMonthInCalendar)
        self.chooseDateInCalendar(self._DayInCalendarFrom, self._DayInCalendarTo)
        self.clickSearchButton(self._SearchButton)
        self.filterByStar(self._FilterByStarInCheckBox)
        self.countFoundAccomodation(self._check1, self._ObjectsOnSearchList, self._ValueToSearch)

if __name__ == "__main__":
    unittest.main()
