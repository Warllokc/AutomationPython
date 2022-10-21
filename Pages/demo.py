from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import LoginLocators

browser = webdriver.Chrome("/automation/WebAutomation/Pages/chromedriver")
browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
# browser.maximize_window()
try:
    UsernameTextField = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, LoginLocators.UsernameTextField)))
    UsernameTextField.send_keys('Admin')

    PasswordTextField = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, LoginLocators.PasswordTextField)))
    PasswordTextField.send_keys('admin123')

    LoginButton = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, LoginLocators.LoginButton)))
    LoginButton.click()
    #
    # EmploymentStatusDropDownButton = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, HomePageLocators.EmploymentStatusDropDownButton)))
    # EmploymentStatusDropDownButton.click()
    #
    # DropDownList = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, HomePageLocators.DropDownList)))
    # DropDownList.click()
    #
    # DropDownText = browser.find_element(By.XPATH, HomePageLocators.EmploymentStatusUpdated).text
    # assert DropDownText == 'Part-Time Contract'
    # # assertEqual(DropDownText, "Part-Time Contract")
    #
    # print(DropDownText)
    # print ("Page is ready!")
except TimeoutException:
    print ("Loading took too much time!")

time.sleep(2)

browser.quit()
# browser.find_element(By.XPATH, "//*[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
# browser.find_element(By.ID, "//*[@class='oxd-button oxd-button--medium oxd-button--first']")


# browser.find_element((By.ID, "alex")).click

