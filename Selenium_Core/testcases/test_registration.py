from Selenium_Core.utility import base
from Selenium_Core.Pages import registration_page
import pytest


def dataset():
    data_for_form = [
        ["Test_1", "Tester1", "Single", "Reading", "India", "1", "1", "2014", "126678938", "tester123",
         "Test123@gmail.com", "Hey welcome to way2automation", "Test!123", "Test!123"],
        ["Test_2", "Tester2", "Married", "Cricket", "India", "1", "1", "2014", "126678939", "tester124",
         "Test124@gmail.com", "Hey welcome to way2automation", "Test!123", "Test!123"],
        ["Test_3", "Tester3", "Divorced", "Reading", "India", "1", "1", "2014", "126678933", "tester125",
         "Test125@gmail.com", "Hey welcome to way2automation", "Test!123", "Test!123"],
        ["Test_4", "Tester4", "Single", "Cricket", "India", "1", "1", "2014", "126678936", "tester126",
         "Test126@gmail.com", "Hey welcome to way2automation", "Test!123", "Test!123"]
    ]
    return data_for_form


@pytest.mark.parametrize("td", dataset())
#td - testData
def test_enter_data_in_form(td):
    browser = base.open_browser("https://www.way2automation.com/way2auto_jquery/registration.php#load_box")
    page = registration_page.registration_info(browser)
    page.enter_first_name(td[0])
    page.enter_last_name(td[1])
    page.enter_marital_status(td[2])
    page.enter_hobby(td[3])
    page.select_country(td[4])
    page.select_month(td[5])
    page.select_day(td[6])
    page.select_year(td[7])
    page.enter_phone_number(td[8])
    page.enter_phone_number(td[9])
    page.enter_email(td[10])
    page.upload_image("/Users/akhilaprakash/PycharmProjects/pythonSeleniumProject/Selenium_Core/testcases/Apple.jpeg")
    page.enter_about_yourself(td[11])
    page.enter_password(td[12])
    page.enter_confirm_password(td[13])
    page.click_on_submit_button()
