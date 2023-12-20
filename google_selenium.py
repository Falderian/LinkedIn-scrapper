from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils import untilWait, convertToCsv
from time import sleep
from upload import uploadCsv


def pressence_check(target):
    return untilWait(driver, target)


results = []

position = "CEO"
region = "USA"

url = "https://www.google.com/"

url_query = f"site:linkedin.com/in/ AND {position} AND {region}"

options = webdriver.ChromeOptions()
# options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.set_window_size(800, 800)

driver.get(url)

try:
    search_input = driver.find_element(By.TAG_NAME, "textarea")
    search_input.send_keys(url_query)
    search_input.submit()
except Exception as e:
    raise Exception("Cookies error")


sleep(1)

for i in range(0, 6):
    driver.find_element(By.TAG_NAME, "html").send_keys(Keys.END)
    sleep(1)

while True:
    try:
        load_more_btn = driver.find_element(By.CLASS_NAME, "GNJvt.ipz2Oe")
        load_more_btn.click()
        sleep(2)
    except Exception as e:
        break

elems = driver.find_elements(By.CLASS_NAME, "yuRUbf")
for elem in elems:
    link = elem.find_element(By.TAG_NAME, "a").get_attribute("href")
    title = elem.find_element(By.TAG_NAME, "h3").get_attribute("innerText")
    results.append((title, link))

convertToCsv("data.csv", results)
uploadCsv()
