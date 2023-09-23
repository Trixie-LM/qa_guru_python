import pytest
from selene.support.shared import browser


@pytest.fixture(autouse=True)
def open_browser():
    browser.config.window_width = 1900
    browser.config.window_height = 1300
    browser.open('https://google.com')
    yield
    browser.quit()



