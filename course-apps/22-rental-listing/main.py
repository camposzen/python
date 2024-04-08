import time
from bs4 import BeautifulSoup
import requests
import selenium.webdriver.common.by
from selenium import webdriver

# Scrap listings from zillow
url = "https://www.zillow.com/san-francisco-ca/rentals/"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "html.parser")

all_anchors = soup.select(selector="article div div a")
links = []
for a in all_anchors:
    links.append(f"https://www.zillow.com/{a['href']}")
links = list(dict.fromkeys(links))  # removing duplicates

all_spans = soup.find_all('span', {'data-test': 'property-card-price'})
prices = []
for s in all_spans:
    prices.append(s.text)

all_addr = soup.find_all('address')
addresses = []
for a in all_addr:
    addresses.append(a.text)

# Fill the form
chrome_driver_path = "/chromedriver_mac64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
form_link = \
    "https://docs.google.com/forms/d/e/1FAIpQLSdYAxVMBXRwaA4AALe4fHK-pOCinwu5ki1gHeqGV--3O93mFg/viewform?usp=sf_link"

for i in range(len(links)):
    driver.get(form_link)
    time.sleep(2)

    inputs = driver.find_elements(by=selenium.webdriver.common.by.By.CSS_SELECTOR, value="input")
    inputs[0].send_keys(links[i])
    inputs[1].send_keys(prices[i])
    inputs[2].send_keys(addresses[i])

    submit_button = driver.find_element(
        by=selenium.webdriver.common.by.By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()

driver.quit()

