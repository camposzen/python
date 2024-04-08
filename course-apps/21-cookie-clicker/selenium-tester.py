import selenium.webdriver.common.by
from selenium import webdriver

chrome_driver_path = "/chromedriver_mac64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
#
# element = driver.find_element(by=selenium.webdriver.common.by.By.ID, value="id-search-field")
# print(element)
#
# logo = driver.find_element(by=selenium.webdriver.common.by.By.CLASS_NAME, value="python-logo")
# print(logo.size)
#
# link = driver.find_element(by=selenium.webdriver.common.by.By.CSS_SELECTOR, value=".documentation-widget a")
# print(link.text)
#
# issue = driver.find_element(by=selenium.webdriver.common.by.By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(issue.text)

# event_widget = driver.find_element(by=selenium.webdriver.common.by.By.CLASS_NAME, value="event-widget")
# print(event_widget)
#
# event_list = event_widget.find_elements(by=selenium.webdriver.common.by.By.CSS_SELECTOR, value="li")
# print(len(event_list))
#
# result = {}
# for i in range(0, len(event_list) - 1):
#     time = event_list[i].find_element(by=selenium.webdriver.common.by.By.CSS_SELECTOR, value="time").text
#     event = event_list[i].find_element(by=selenium.webdriver.common.by.By.CSS_SELECTOR, value="a").text
#     result[i] = {time: event}
# print(result)

event_times = driver.find_elements(by=selenium.webdriver.common.by.By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(by=selenium.webdriver.common.by.By.CSS_SELECTOR, value=".event-widget li a")
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)
    
# driver.close()
driver.quit()

