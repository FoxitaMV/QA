import pytest
from mobile import mobile_test_main_page
from mobile import mobile_test_service_form
from mobile import mobile_test_testdrive_form
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def mobile_testdrive_form():
    text = 'Заявка отправлена'
    assert (text in mobile_test_testdrive_form.ts.driver.page_source)
mobile_testdrive_form()

def mobile_main_page_form():
    text = 'Сообщение отправлено'
    assert (text in mobile_test_main_page.ts.driver.page_source)
mobile_main_page_form()

def mobile_service_page_form():
    text = "Сообщение отправлено! =)"
    assert (text in mobile_test_service_form.ts.driver.page_source)
mobile_service_page_form()