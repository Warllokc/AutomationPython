import automation.WebAutomation.Tests.test_config as conf
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_open_page():
    # OPEN THE BROWSER/(MAKE SURE 'chromedriver' IS UPDATED TO THE VERSION OF YOUR CHROME)
    conf.browser.get(conf.URL)
    conf.browser.maximize_window()
    assert conf.browser.title == conf.page_title

def test_login():
    try:
        UsernameTextField = WebDriverWait(conf.browser, 2).until(EC.presence_of_element_located(
            (By.XPATH, LoginLocators.UsernameTextField)))
        UsernameTextField.send_keys(conf.username)

        PasswordTextField = WebDriverWait(conf.browser, 2).until(EC.presence_of_element_located(
            (By.XPATH, LoginLocators.PasswordTextField)))
        PasswordTextField.send_keys(conf.password)

        LoginButton = WebDriverWait(conf.browser, 2).until(EC.presence_of_element_located(
            (By.XPATH, LoginLocators.LoginButton)))
        LoginButton.click()

        LandingPageLoggedUserName = conf.browser.find_element(By.XPATH, HomePageLocators.LandingPageLoggedUserName).text
        assert LandingPageLoggedUserName == conf.userName

        conf.browser.quit()

    except TimeoutException:
        print("Loading took too much time!")



