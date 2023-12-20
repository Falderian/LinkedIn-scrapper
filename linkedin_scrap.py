from selenium import webdriver
from time import sleep
from utils import untilWait
from login import login_user
from search import search


def run_scrapper():
    region_to_search = "Africa"

    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    # options.add_argument("--width=1025")

    driver = webdriver.Chrome(options=options)

    def pressence_check(target):
        return untilWait(driver, target)

    login_user(driver)
    search(driver, pressence_check, region_to_search, sleep)


run_scrapper()
