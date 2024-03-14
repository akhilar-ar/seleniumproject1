import configparser


def readLocator(section, key):
    reader = configparser.ConfigParser()
    reader.read("/Users/akhilaprakash/PycharmProjects/pythonSeleniumProject/E2E_Framework/ConfigData/locators.cfg")
    return reader.get(section, key)

a= readLocator("Registration", "about")
print(a)