import pytest
from selene.support.shared import browser


@pytest.fixture()
def open_browser():
    browser.config.window_width = 1900
    browser.config.window_height = 1600
    browser.open('https://google.com')
    yield




