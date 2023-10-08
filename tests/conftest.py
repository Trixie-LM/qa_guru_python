import pytest
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def our_browser():
    currenr_name = os.path.abspath((__file__))
    currenr_dir = os.path.dirname(currenr_name)
    if not os.path.exists('tmp'):
        os.mkdir('tmp')
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": os.path.join(currenr_dir, 'tmp'),
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    service = Service('../resources/chromedriver.exe')

    driver = webdriver.Chrome(service=service, options=options)
    yield
    # Удаление директории
    # os.rmdir(os.path.join(currenr_dir, 'tmp'))
