from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def untilWait(browser, target):
    return (
        WebDriverWait(browser, 20)
        .until(EC.visibility_of_element_located(target))
        .click()
    )
