from cProfile import label

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Selenium_Core.utility import common
#from selenium import webdriver
#browser=webdriver.Chrome()



class registration_info:

    def __init__(self, browser):
        self.browser = browser
        section = "Registration"
        self.Name_firstname = common.getLocator(section,"Name_firstname")
        self.XPATH_lastname = common.getLocator(section,"XPATH_lastname")
        self.XPATH_maritalStatus = common.getLocator(section,"XPATH_maritalStatus")
        self.XPATH_hobby = common.getLocator(section, "XPATH_hobby")
        self.XPATH_country = common.getLocator(section,"XPATH_country")
        self.XPATH_month = common.getLocator(section,"XPATH_month")
        self.XPATH_day = common.getLocator(section,"XPATH_day")
        self.XPATH_year = common.getLocator(section,"XPATH_year")
        self.Name_phoneNumber = common.getLocator(section,"Name_phoneNumber")
        self.Name_username = common.getLocator(section,"Name_username")
        self.Name_email = common.getLocator(section,"NAME_email")
        self.XPATH_upload = common.getLocator(section,"XPATH_upload")
        self.TAGNAME_about = common.getLocator(section,"TAGNAME_about")
        self.Name_password = common.getLocator(section, "Name_password")
        self.Name_confirmPassword = common.getLocator(section,"Name_confirmPassword")
        self.XPATH_submit = common.getLocator(section, "XPATH_submit")




    def enter_first_name(self, first_name):
        self.browser.find_element(By.NAME, self.Name_firstname).send_keys(first_name)

    def enter_phone_number(self, phone):
        self.browser.find_element(By.NAME, self.Name_phoneNumber).send_keys(phone)

    def enter_username(self, username):
        self.browser.find_element(By.NAME, self.Name_username).send_keys(username)

    def enter_email(self, email):
        self.browser.find_element(By.NAME, self.Name_email).send_keys(email)

    def enter_password(self, password):
        self.browser.find_element(By.NAME, self.Name_password).send_keys(password)

    def enter_confirm_password(self, c_password):
        self.browser.find_element(By.NAME, self.Name_confirmPassword).send_keys(c_password)

    def enter_last_name(self, last_name):
        self.browser.find_element(By.XPATH, "//label[text()='Last Name:']/following-sibling::input").send_keys(last_name)

    def enter_marital_status(self, status):
        self.browser.find_element(By.XPATH, "//label[text()=' "+status+"']/input").click()

    def enter_hobby(self, hobby):
        self.browser.find_element(By.XPATH, "//label[text()=' "+hobby+"']/input").click()

    def select_country(self, country):
        dd=Select(self.browser.find_element(By.XPATH, self.XPATH_country))
        dd.select_by_visible_text(country)

    def select_month(self, month):
        dd = Select(self.browser.find_element(By.XPATH, self.XPATH_month))
        dd.select_by_visible_text(month)

    def select_day(self, day):
        dd=Select(self.browser.find_element(By.XPATH, self.XPATH_day))
        dd.select_by_visible_text(day)

    def select_year(self, year):
        dd = Select(self.browser.find_element(By.XPATH, self.XPATH_year))
        dd.select_by_visible_text(year)

    def upload_image(self,file_path):
        self.browser.find_element(By.XPATH,self.XPATH_upload).send_keys(file_path)

    def enter_about_yourself(self, inputText):
        self.browser.find_element(By.TAG_NAME, self.TAGNAME_about).send_keys(inputText)


    def click_on_submit_button(self):
        self.browser.find_element(By.XPATH, self.XPATH_submit).click()

























