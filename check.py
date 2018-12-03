from selenium import webdriver

driver = webdriver.Chrome()
try:
    driver.get('http://python.org')
    input('W nowym oknie Chrome powinna załadować się strona python.org')
finally:
    driver.quit()

