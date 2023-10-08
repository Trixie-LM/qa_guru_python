import os.path
import time

import requests
from selene import query
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selene.support.shared import browser


def test_download_file_with_selene_by_href():
    browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")

    href = browser.element("[data-testid='raw-button']").get(query.attribute("href"))
    content = requests.get(href).content
    with open("pytest_readme.rst", "wb")as f:
        f.write(content)

    with open("pytest_readme.rst")as f:
        text = f.read()
        assert "framework makes it easy to write" in text


def test_download_file_with_selene_by_button():
    currenr_dir = os.path.dirname(os.path.abspath((__file__)))
    if not os.path.exists('tmp'):
        os.mkdir('tmp')
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": os.path.join(currenr_dir, 'tmp'),
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    service = Service('../chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)

    browser.config.driver = driver
    browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")
    browser.element("[data-testid='download-raw-button']").click()
    time.sleep(5)
    with open("tmp/readme.rst") as f:
        text = f.read()
        assert "framework makes it easy to write" in text
