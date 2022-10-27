import automation.WebAutomation.Tests.test_config as conf
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import automation.WebAutomation.Pages.HomePageLocators as homePageLocators
import automation.WebAutomation.Pages.LoginLocators as loginLocators


def test_open_page():
    # OPEN THE BROWSER/(MAKE SURE 'chromedriver' IS UPDATED TO THE VERSION OF YOUR CHROME)
    conf.browser.get(conf.URL)
    conf.browser.maximize_window()
    assert conf.browser.title == conf.page_title

def test_login():
    try:
        UsernameTextField = WebDriverWait(conf.browser, 2).until(EC.presence_of_element_located(
            (By.XPATH, loginLocators.UsernameTextField)))
        UsernameTextField.send_keys(conf.username)

        PasswordTextField = WebDriverWait(conf.browser, 2).until(EC.presence_of_element_located(
            (By.XPATH, loginLocators.PasswordTextField)))
        PasswordTextField.send_keys(conf.password)

        LoginButton = WebDriverWait(conf.browser, 2).until(EC.presence_of_element_located(
            (By.XPATH, loginLocators.LoginButton)))
        LoginButton.click()

        LandingPageLoggedUserName = conf.browser.find_element(By.XPATH, homePageLocators.LandingPageConfiguration).text
        assert LandingPageLoggedUserName == conf.LandingPageConfiguration

        conf.browser.quit()

    except TimeoutException:
        print("Loading took too much time!")



