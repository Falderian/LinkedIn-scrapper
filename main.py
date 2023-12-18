from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from utils import untilWait

login_url = "https://www.linkedin.com/"
search_url = "https://www.linkedin.com/search/results/companies"
login = "luciimportant@wireconnected.com"
passw = 95546209554620
user = [login, passw]
company_to_search = "Cyfrania"

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)


def checkHtmlExists(target):
    return untilWait(driver, target)


driver.get(login_url)
input_target = (
    By.CLASS_NAME,
    "text-color-text.font-sans.text-md.outline-0.bg-color-transparent.grow",
)

checkHtmlExists(input_target)
inputs = driver.find_elements(*input_target)
for input in inputs:
    index = inputs.index(input)
    input.send_keys(user[index])

submit_btn = driver.find_element(
    By.CSS_SELECTOR, ".btn-md.btn-primary.flex-shrink-0.cursor-pointer"
)

submit_btn.click()

driver.get(search_url)

search_target = (By.CLASS_NAME, "search-global-typeahead__input")

checkHtmlExists(search_target)

search_input = driver.find_element(*search_target)
search_input.send_keys(company_to_search)
search_input.send_keys(Keys.ENTER)

search_res = (By.CLASS_NAME, "reusable-search__result-container")

checkHtmlExists(search_res)

search_results_target = driver.find_element(*search_res)
search_results_target.click()

button_target = (
    By.CSS_SELECTOR,
    ".active.ember-view.pv3.ph4.t-16.t-bold.t-black--light.org-page-navigation__item-anchor",
)

checkHtmlExists(button_target)

btns = driver.find_elements(*button_target)
print(len(btns))
sleep(60)
