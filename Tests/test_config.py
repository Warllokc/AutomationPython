from selenium import webdriver
from random import randint

browser = webdriver.Chrome('<path to your chromedriver>')

URL = 'https://opensource-demo.orangehrmlive.com/'
logi_icon_css = "#divLogo"
username_textfield_css = "#txtUsername"
password_textfield_css = "#txtPassword"
submit_button_css = "#btnLogin"
forgot_password_xpath = "//*[contains(text(),'Forgot your` password?')]"

page_title = "OrangeHRM"

username = 'Admin'
password = 'admin123'

LandingPageDashboard = 'Dashboard'
EmployeeFullNameText = "Employee Full Name"

newUserFirstName = 'Iulian'
newUserLastName = 'Bondari'

employeeInformationText = 'Employee Information'

personalDetailsText = 'Personal Details'

employeeID = str(randint(200, 10000))
