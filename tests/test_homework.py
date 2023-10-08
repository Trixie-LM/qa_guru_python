import time
import requests
from selene import query
from selene.support.shared import browser


def test_download_file_with_selene_by_href():
    browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")

    href = browser.element("[data-testid='raw-button']").get(query.attribute("href"))
    content = requests.get(href).content
    with open("pytest_readme.rst", "wb") as f:
        f.write(content)

    with open("pytest_readme.rst") as f:
        text = f.read()
        assert "framework makes it easy to write" in text


def test_download_file_with_selene_by_button(our_browser):
    browser.config.driver = our_browser

    browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")
    browser.element("[data-testid='download-raw-button']").click()
    time.sleep(3)
    with open("tmp/README.rst") as f:
        text = f.read()
        assert "framework makes it easy to write" in text
