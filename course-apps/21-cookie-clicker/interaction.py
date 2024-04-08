import selenium.webdriver.common.by
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


chrome_driver_path = "/chromedriver_mac64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles_count = driver.find_element(by=selenium.webdriver.common.by.By.CSS_SELECTOR, value="#articlecount a")
print(articles_count.text)
# articles_count.click()

# all_portals = driver.find_element(by=selenium.webdriver.common.by.By.LINK_TEXT, value="All portals")
# all_portals.click()

search = driver.find_element(by=selenium.webdriver.common.by.By.NAME, value="search")
print(search)
search.send_keys("Python", selenium.webdriver.Keys.ENTER)

my_element_id = 'Python'
ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
WebDriverWait(driver, 5, ignored_exceptions=(NoSuchElementException, StaleElementReferenceException))
driver.quit()
