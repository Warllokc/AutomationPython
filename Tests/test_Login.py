import pytest
import allure
import AutomationPython.Tests.test_config as conf
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import AutomationPython.Pages.HomePageLocators as homePageLocators
import AutomationPython.Pages.LoginLocators as loginLocators

@pytest.fixture(scope="module")
def browser():
    browser = conf.browser
    yield browser
    browser.close()

def test_open_page(browser, request):
    # OPEN THE BROWSER/(MAKE SURE 'chromedriver' IS UPDATED TO THE VERSION OF YOUR CHROME)
    browser.get(conf.URL)
    browser.maximize_window()
    assert browser.title == conf.page_title

    # Add screenshot to the report
    file_name = f"{request.node.name}.png"
    browser.save_screenshot(file_name)
    with open(file_name, "rb") as f:
        screenshot = f.read()
    allure.attach(screenshot, file_name, allure.attachment_type.PNG)


def test_login(browser, request):
    try:
        UsernameTextField = WebDriverWait(browser, 2).until(EC.presence_of_element_located(
            (By.XPATH, loginLocators.UsernameTextField)))
        UsernameTextField.send_keys(conf.username)

        PasswordTextField = WebDriverWait(browser, 2).until(EC.presence_of_element_located(
            (By.XPATH, loginLocators.PasswordTextField)))
        PasswordTextField.send_keys(conf.password)

        LoginButton = WebDriverWait(browser, 2).until(EC.presence_of_element_located(
            (By.XPATH, loginLocators.LoginButton)))
        LoginButton.click()
        time.sleep(5)
        LandingPageLoggedUserName = browser.find_element(By.XPATH, homePageLocators.LandingPageDashboard).text
        assert LandingPageLoggedUserName == conf.LandingPageDashboard

        # Add screenshot to the report
        file_name = f"{request.node.name}.png"
        browser.save_screenshot(file_name)
        with open(file_name, "rb") as f:
            screenshot = f.read()
        allure.attach(screenshot, file_name, allure.attachment_type.PNG)

    except TimeoutException:
        print("Loading took too much time!")

    # Add screenshot to the report
    file_name = f"{request.node.name}.png"
    browser.save_screenshot(file_name)
    with open(file_name, "rb") as f:
        screenshot = f.read()
    allure.attach(screenshot, file_name, allure.attachment_type.PNG)

