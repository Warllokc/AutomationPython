from selenium import webdriver

browser = webdriver.Chrome('/Users/alexandrpetricenco/Desktop/Python_tricks/automation/WebAutomation/Pages/chromedriver')

URL = 'https://opensource-demo.orangehrmlive.com/'
logi_icon_css = "#divLogo"
username_textfield_css = "#txtUsername"
password_textfield_css = "#txtPassword"
submit_button_css = "#btnLogin"
forgot_password_xpath = "//*[contains(text(),'Forgot your` password?')]"

page_title = "OrangeHRM"

username = 'Admin'
password = 'admin123'

LandingPageConfiguration = 'Configuration'