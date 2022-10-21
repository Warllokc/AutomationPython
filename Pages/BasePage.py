from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""Parent of all pages """
"""it contains all generic matheds and utilities for all the pages"""

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self,by_locator):
        WebDriverWait(self.driver)