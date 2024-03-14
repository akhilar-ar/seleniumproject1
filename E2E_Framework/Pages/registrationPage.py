from selenium import webdriver
from selenium.webdriver.common.by import By
from E2E_Framework.Base import locatorReader
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()



class reg:

    def __init__(self, focusFromPreviousHandle, section):
        global driver
        driver = focusFromPreviousHandle
        self.section = section

    def enterDataUsingXpath(self, locator, data):
        driver.find_element(By.XPATH, locatorReader.readLocator(self.section, locator)).send_keys(data)

    def enterDataUsingName(self, locator, data):
        driver.find_element(By.NAME, locatorReader.readLocator(self.section, locator)).send_keys(data)

    def enterDataUsingTagName(self, locator, data):
        driver.find_element(By.TAG_NAME, locatorReader.readLocator(self.section, locator)).send_keys(data)

    def clickOnElement(self, element):
        driver.find_element(By.XPATH, locatorReader.readLocator(self.section, element)).click()

    def selectItemFromDropdown(self, locator, itemToBeSelected):
        dd = Select(driver.find_element(By.XPATH, locatorReader.readLocator(self.section, locator)))
        dd.select_by_visible_text(itemToBeSelected)



