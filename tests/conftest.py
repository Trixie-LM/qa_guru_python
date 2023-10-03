import pytest
from selene.support.shared import browser
from selene import have


@pytest.fixture(scope='function', autouse=True)
def browser_management():

    # Browser settings
    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1900
    browser.config.window_height = 1600
    browser.config.timeout = 6.0
    yield
    browser.quit()



