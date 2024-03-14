from E2E_Framework.Base import InitialiseDriver, common
from E2E_Framework.Pages import resize


def test_resizeItemByWidth():
    browser = InitialiseDriver.startBrowser("https://www.way2automation.com/way2auto_jquery/resizable.php#load_box")
    r = resize.Resize(browser, "Resize")
    c = common.CommonMethods(browser)
    c.switchToIframe("XPATH_iFrame", "Resize")
    beforeMoving = c.findHeightAndWidthID("ID_resizeBox", "Resize", "width")
    r.resizeArea("draggingPoint", 600, 0)
    afterMoving = c.findHeightAndWidthID("ID_resizeBox", "Resize", "width")
    assert (afterMoving - beforeMoving) == 600


def test_resizeItemByHeight():
    browser = InitialiseDriver.startBrowser("https://www.way2automation.com/way2auto_jquery/resizable.php#load_box")
    r = resize.Resize(browser, "Resize")
    c = common.CommonMethods(browser)
    c.switchToIframe("XPATH_iFrame", "Resize")
    beforeMoving = c.findHeightAndWidthID("ID_resizeBox", "Resize", "height")
    r.resizeArea("draggingPoint", 0, 100)
    afterMoving = c.findHeightAndWidthID("ID_resizeBox", "Resize", "height")
    assert (afterMoving - beforeMoving) == 100