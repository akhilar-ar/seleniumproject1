from selenium import webdriver

# chromedriver
driver = webdriver.Chrome()

"""
Firefox --> geckodriver
Edge --> 
"""


def startBrowser(url):
    """
    This is to start chromebroswer and open wa2automation website
    :return:
    """

    driver.get(url)
    driver.maximize_window()
    return driver


def stopBrowser():

    """
    This is to stop the browser
    :return:
    """
    driver.quit()

"""
[Section]
key = value
"""