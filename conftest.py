import allure
import pytest
from selenium import webdriver



@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item) -> str:
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep



@pytest.fixture(scope="function")
def web_driver(request):
    driver = webdriver.Firefox()
    yield driver
    if request.node.rep_call.failed:
        try:
            allure.attach(driver.get_screenshot_as_png(), name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
        except:
            pass
    print("\n Закрытие браузера\n browser quit")
    driver.quit()

