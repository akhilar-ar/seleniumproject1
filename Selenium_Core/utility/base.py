from selenium import webdriver

load_browser = webdriver.Chrome()

def open_browser(URL):
    load_browser.get(URL)
    load_browser.maximize_window()
    return load_browser

def stop_browser(URL):
    load_browser.quit()


open_browser("https://www.way2automation.com/way2auto_jquery/registration.php#load_box")




