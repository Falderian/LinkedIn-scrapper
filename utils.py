from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import getcwd
import csv


def untilWait(browser, target):
    return (
        WebDriverWait(browser, 20)
        .until(EC.visibility_of_element_located(target))
        .click()
    )


def convertToCsv(filename: str, data: list[str]):
    column_names = ["title", "link"]
    path_to_sheets_dir = getcwd() + "/" + filename

    with open(path_to_sheets_dir, "w", newline="") as file:
        write = csv.writer(file)

        write.writerow(column_names)
        write.writerows(data)
