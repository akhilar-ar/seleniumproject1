from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from E2E_Framework.Base import locatorReader


# driver = webdriver.Chrome()


class CommonMethods:
    def __init__(self, focusFromPreviousHandle):
        global driver
        driver = focusFromPreviousHandle

    def switchToIframe(self, locator, section):
        element = driver.find_element(By.XPATH, locatorReader.readLocator(section, locator))
        driver.switch_to.frame(element)

    def verifyIfElementIsVisible(self, locator, section):
        try:
            check = driver.find_element(By.XPATH, locatorReader.readLocator(section, locator))
            return True
        except NoSuchElementException:
            return False

    def findPositionOnAnyAxisByXpath(self, locator, section, typeOfAxis):
        item = driver.find_element(By.XPATH, locatorReader.readLocator(section, locator))
        axis = item.location.get(typeOfAxis)
        return axis

    def findHeightAndWidthXPATH(self, locator, section, typeofAttribute):
        item = driver.find_element(By.XPATH, locatorReader.readLocator(section, locator))
        area = item.size.get(typeofAttribute)
        return area

    #def findHeightAndWidthID(self, locator, section, typeofAttribute):
    #    item = driver.find_element(By.ID, locatorReader.readLocator(section, locator))
    #    area = item.size.get(typeofAttribute)
    #    return area
