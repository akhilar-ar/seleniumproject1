import time

from E2E_Framework.Base import InitialiseDriver, locatorReader, common
from E2E_Framework.Pages import registrationPage, drag


def test_verifyDragWorkingOnXAxis():
    browser = InitialiseDriver.startBrowser("https://www.way2automation.com/way2auto_jquery/draggable.php#load_box")
    d = drag.Drag(browser, "Drag")
    c = common.CommonMethods(browser)
    c.switchToIframe("XPATH_iFrame", "Drag")
    beforeDragPosition = d.findCurrentPositionOfElement("ID_dragBox")
    d.dragAndDrop("id_dragBox")
    afterDragPosition = d.findCurrentPositionOfElement("ID_dragBox")
    assert (afterDragPosition - beforeDragPosition) == 800  # verifying the drag position
    time.sleep(4)


def test_dragAndDropToDestination():
    browser = InitialiseDriver.startBrowser("https://www.way2automation.com/way2auto_jquery/droppable.php#load_box")
    d = drag.Drag(browser, "Drag")
    c = common.CommonMethods(browser)
    c.switchToIframe("XPATH_iFrame2", "Drag")
    d.dragAndDropToDestination("ID_dragBox", "ID_dropBox")
    expected = c.verifyIfElementIsVisible("XPATH_highlight", "Drag")
    assert expected == True
    time.sleep(3)





