from selenium.webdriver.common.by import By
from E2E_Framework.Base import locatorReader
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class Drag:
    def __init__(self, focusFromPreviousHandle, section):
        global driver
        driver = focusFromPreviousHandle
        self.section = section

    def findCurrentPositionOfElement(self, locator):
        element = driver.find_element(By.ID, locatorReader.readLocator(self.section, locator))
        location = element.location
        x = location.get('x')
        return x

    def dragAndDrop(self, locator):
        action = ActionChains(driver) #driver: focus
        action.drag_and_drop_by_offset(driver.find_element(By.ID, locatorReader.readLocator(self.section, locator)), 800, 0 )
        action.perform()

    def dragAndDropToDestination(self, source, destination):
        action = ActionChains(driver)
        action.drag_and_drop(driver.find_element(By.ID, locatorReader.readLocator(self.section, source)), (driver.find_element(By.ID, locatorReader.readLocator(self.section, destination))))
        action.perform()





