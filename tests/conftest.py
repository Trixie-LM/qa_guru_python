import pytest
from selene.support.shared import browser


@pytest.fixture(autouse=True)
def open_browser():
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1900
    browser.config.window_height = 1600
    browser.open('https://demoqa.com/automation-practice-form')
    yield
    browser.quit()



