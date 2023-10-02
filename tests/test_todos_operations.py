from selene.support.shared import browser
from selene import be, have, command


def test_apply_form():
    browser.element('#firstName').should(be.blank).type('Pinkamena').press_enter()
    browser.element('#lastName').should(be.blank).type('Pie').press_enter()
    browser.element('#userEmail').should(be.blank).type('Cakes_and_bakery@mail.com').press_enter()
    # browser.element('#gender-radio-2').should(be.blank).click()
    browser.element('#userNumber').should(be.blank).type('79991234567').press_enter()
    # browser.element('#dateOfBirthInput').should(be.blank).click()
    # browser.element('#hobbies-checkbox-1').click()
    browser.element('#currentAddress').should(be.blank).type('Sugar Palace, a candy store in Ponyville.')
    browser.element('.css-19bqh2r').click()
    browser.element('#submit').click()
