import time

from E2E_Framework.Base import InitialiseDriver, locatorReader
from E2E_Framework.Pages import registrationPage


def test_verifyRegistrationHappens():
    path = "/Users/akhilaprakash/PycharmProjects/pythonSeleniumProject/E2E_Framework/ConfigData/RedApple.jpg"
    browser = InitialiseDriver.startBrowser("https://www.way2automation.com/way2auto_jquery/registration.php#load_box")
    r = registrationPage.reg(browser, "Registration")
    time.sleep(3)
    r.enterDataUsingXpath("firstName", "Akhila")
    r.enterDataUsingXpath("lastName", " Prakash")
    r.clickOnElement("mStatus")
    r.clickOnElement("hobby")
    r.selectItemFromDropdown("country", "India")
    r.selectItemFromDropdown("month", "1")
    r.selectItemFromDropdown("day", "1")
    r.selectItemFromDropdown("year", "2014")
    r.enterDataUsingName("phone", "7693747582")
    r.enterDataUsingName("username", "mynameisAK")
    r.enterDataUsingName("email", "ak@gmail.com")
    r.enterDataUsingXpath("file", path)
    r.enterDataUsingTagName("about", "This is a tagName")
    r.enterDataUsingName("password", "test123!")
    r.enterDataUsingName("confirmPassword", "test123!")
    time.sleep(2)
    r.clickOnElement("submit")

