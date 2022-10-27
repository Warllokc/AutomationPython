import time
from selenium.webdriver.common.keys import Keys
import automation.WebAutomation.Tests.test_config as conf
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import automation.WebAutomation.Pages.HomePageLocators as homePageLocators
import automation.WebAutomation.Pages.LoginLocators as loginLocators
import automation.WebAutomation.Pages.addEmployeePage as addEmployeePage
import automation.WebAutomation.Pages.employeeListPage as employeeListPage
import automation.WebAutomation.Pages.personalDetailsPage as personalDetailsPage

employeeIDNumber = conf.employeeID

def test_open_page():
    # OPEN THE BROWSER/(MAKE SURE 'chromedriver' IS UPDATED TO THE VERSION OF YOUR CHROME)
    conf.browser.get(conf.URL)
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

            LandingPageLoggedUserName = conf.browser.find_element(By.XPATH,
                                                                  homePageLocators.LandingPageConfiguration).text
            assert LandingPageLoggedUserName == conf.LandingPageConfiguration

        except TimeoutException:
            print("Loading took too much time!")

def test_clickAddEmployee():
    LandingPageAddEmployee = WebDriverWait(conf.browser, 2).until(EC.presence_of_element_located(
        (By.XPATH, homePageLocators.LandingPageAddEmployee)))
    LandingPageAddEmployee.click()

    AddEmployeeMenu = conf.browser.find_element(By.XPATH, homePageLocators.AddEmployeeMenu).text
    assert AddEmployeeMenu == conf.EmployeeFullNameText

def test_addNewEmployeeCancelButton():
    firstName = WebDriverWait(conf.browser, 2).until(EC.presence_of_element_located(
        (By.XPATH, addEmployeePage.firstName)))
    firstName.click()
    firstName.send_keys(conf.newUserFirstName)

    lastName = WebDriverWait(conf.browser, 2).until(EC.presence_of_element_located(
        (By.XPATH, addEmployeePage.lastName)))
    lastName.click()
    lastName.send_keys(conf.newUserLastName)



    cancelButton = WebDriverWait(conf.browser, 2).until(EC.presence_of_element_located(
        (By.XPATH, addEmployeePage.cancelButton)))
    cancelButton.click()

    employeeInformation = conf.browser.find_element(By.XPATH,
                                                          employeeListPage.employeeInformation).text
    assert employeeInformation == conf.employeeInformationText

def test_addNewEmployee():
    LandingPageAddEmployee = WebDriverWait(conf.browser, 2).until(EC.presence_of_element_located(
        (By.XPATH, homePageLocators.LandingPageAddEmployee)))
    LandingPageAddEmployee.click()

    firstName = WebDriverWait(conf.browser, 2).until(EC.presence_of_element_located(
        (By.XPATH, addEmployeePage.firstName)))
    firstName.click()
    firstName.send_keys(conf.newUserFirstName)

    lastName = WebDriverWait(conf.browser, 2).until(EC.presence_of_element_located(
        (By.XPATH, addEmployeePage.lastName)))
    lastName.click()
    lastName.send_keys(conf.newUserLastName)

    employeeID = WebDriverWait(conf.browser, 2).until(EC.presence_of_element_located(
        (By.XPATH, addEmployeePage.employeeID)))
    employeeID.click()
    for i in range(5):
        employeeID.send_keys(Keys.BACKSPACE)

    employeeID.send_keys(employeeIDNumber)

    saveButton = WebDriverWait(conf.browser, 2).until(EC.presence_of_element_located(
        (By.XPATH, addEmployeePage.saveButton)))
    saveButton.click()
    time.sleep(3)
    personalDetailsPageText = conf.browser.find_element(By.XPATH,
                                                          personalDetailsPage.personalDetails).text
    assert personalDetailsPageText == conf.personalDetailsText


def test_clickEmployeeList():
    employeeListButton = WebDriverWait(conf.browser, 2).until(EC.presence_of_element_located(
        (By.XPATH, employeeListPage.employeeListButton)))
    employeeListButton.click()

    employeeInformation = conf.browser.find_element(By.XPATH,
                                                          employeeListPage.employeeInformation).text
    assert employeeInformation == conf.employeeInformationText


    conf.browser.quit()