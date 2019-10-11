import pytest
from pc import test_mainpage_form
from pc import test_testdrive_from
from pc import test_service_form
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def testdrive_form():
    text = 'Заявка отправлена'
    assert (text in test_testdrive_from.ts.driver.page_source)
testdrive_form()

def main_page_form():
    text = 'Сообщение отправлено'
    assert (text in test_mainpage_form.ts.driver.page_source)
main_page_form()

def service_page_form():
    text = "Сообщение отправлено! =)"
    assert (text in test_service_form.ts.driver.page_source)
service_page_form()