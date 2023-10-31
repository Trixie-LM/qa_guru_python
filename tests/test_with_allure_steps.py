import allure
from allure_commons.types import Severity
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "Trixie Lulamoon")
@allure.description("Test with allure steps")
@allure.feature("Search issue on github")
@allure.link('https://github.com', name='Testing')
def test_find_issue_on_github_with_steps():
    with allure.step("Open main page"):
        browser.open("https://github.com")

    with allure.step("Find repository"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("eroshenkoam/allure-example")
        s("#query-builder-test").submit()

    with allure.step("Go to repository"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Go to Issues tab"):
        s("#issues-tab").click()

    with allure.step("Check issue #76"):
        s(by.partial_text("#76")).should(be.visible)

    browser.quit()