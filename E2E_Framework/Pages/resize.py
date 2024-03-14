from selenium.webdriver.common.by import By
from E2E_Framework.Base import locatorReader
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class Resize:
    def __init__(self, focusFromPreviousHandle, section):
        global driver
        driver = focusFromPreviousHandle
        self.section = section

    def resizeArea(self, draggingPoint, x, y):
        actions = ActionChains(driver)
        element = driver.find_element(By.XPATH, locatorReader.readLocator(self.section, draggingPoint))
        actions.click_and_hold(element)
        actions.drag_and_drop_by_offset(element, x, y)
        actions.perform()
