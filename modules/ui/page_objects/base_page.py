from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    PATH = r"/Users/laslo23/prometheus_test/chromedriver"
    DRIVER_NAME = "chromedriver"

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service(BasePage.PATH + BasePage.DRIVER_NAME)
            )

    def close(self):
        self.driver.close()