import allure
from allure_commons.types import Severity
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "Trixie Lulamoon")
@allure.description("Test without allure steps and decorators")
@allure.feature("Search issue on github")
@allure.link('https://github.com', name='Testing')
def test_find_issue_on_github():
    browser.open('https://github.com')

    s(".header-search-button").click()
    s("#query-builder-test").send_keys("eroshenkoam/allure-example")
    s("#query-builder-test").submit()

    s(by.link_text("eroshenkoam/allure-example")).click()

    s("#issues-tab").click()

    s(by.partial_text("#76")).should(be.visible)

    browser.quit()