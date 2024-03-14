import configparser

def getLocator(section,key):
    reader=configparser.ConfigParser()
    reader.read("/Users/akhilaprakash/PycharmProjects/pythonSeleniumProject/Selenium_Core/testdata/locators.cfg")
    return reader.get(section, key)

#a= getLocator("Registration", "XPATH_country")
#print(a)