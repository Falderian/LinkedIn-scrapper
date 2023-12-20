from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def search(driver, pressence_check, region_to_search, sleep):
    search_url = "https://www.linkedin.com/search/results/people/"

    driver.get(search_url)

    locations_btn_target = (By.ID, "searchFilter_geoUrn")
    pressence_check(locations_btn_target)
    locations_btn = driver.find_element(*locations_btn_target)
    locations_btn.click()

    fieldsets_target = (By.TAG_NAME, "fieldset")

    locations_form = driver.find_elements(*fieldsets_target)[1]
    locations_input = locations_form.find_element(By.TAG_NAME, "input")
    locations_input.send_keys(region_to_search)
    locations_btn.click()
    locations_input.click()
    # search_target = (By.CLASS_NAME, "search-global-typeahead__input")
    # search_input = driver.find_element(*search_target)
    # search_input.send_keys("CEO")
    # search_input.send_keys(Keys.ENTER)
    # basic-typeahead__triggered-content
    sleep(60)
