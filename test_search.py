from selene.support.shared import browser
from selene import be, have


def test_search(open_browser):
    browser.element('#APjFqb').should(be.blank).type('yashaka/selene').press_enter()
    assert browser.element('#search').should(have.text('yashaka/selene: User-oriented Web UI browser tests in ...'))


def test_negative_search(open_browser):
    browser.element('#APjFqb').should(be.blank).type('EXRDCFTVYGBHUnjimko,lpkmjnuhbgyft').press_enter()
    assert browser.element('#result-stats').should(have.text('Результатов: примерно 0'))
