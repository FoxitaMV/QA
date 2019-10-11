import pytest
import test_mainpage_form
import test_testdrive_from
import test_service_form
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def test_function_one():
    text = 'Заявка отправлена'
    assert (text in test_testdrive_from.ts.driver.page_source)
test_function_one()

def test_function_two():
    text = 'Сообщение отправлено'
    assert (text in test_mainpage_form.ts.driver.page_source)
test_function_two()

def service_form_send():
    text = "Сообщение отправлено! =)"
    assert (text in test_service_form.ts.driver.page_source)
service_form_send()