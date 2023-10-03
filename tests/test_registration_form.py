import os

from selene.support.shared import browser
from selene import be, have


def test_registration_form():
    # Browser operations
    browser.open('/automation-practice-form')
    browser.should(have.title_containing('DEMOQA'))

    # firstName
    browser.element('#firstName').should(be.blank).type('Pinkamena')

    # lastName
    browser.element('#lastName').should(be.blank).type('Pie')

    # Email
    browser.element('#userEmail').should(be.blank).type('Cakes_and_bakery@mail.com')

    # Gender
    browser.element("label[for='gender-radio-2']").click()

    # Phone
    browser.element('#userNumber').should(be.blank).type('9991234567')

    # Date of Birth
    browser.element('#dateOfBirthInput').click()
    browser.element("[class='react-datepicker__day react-datepicker__day--023']").click()

    # Subjects
    browser.element('#subjectsInput').should(be.blank).type(
      'Maths'
    ).press_enter()

    # Hobbies
    browser.element("label[for='hobbies-checkbox-3']").click()

    # Picture
    browser.element("#uploadPicture").send_keys(os.path.abspath('image/Trixie.jpeg'))

    # Current Address
    browser.element('#currentAddress').should(be.blank).type('Sugar Palace, a candy store in Ponyville.')

    # State
    browser.element('#state').click()
    browser.element('#react-select-3-option-2').click()

    # City
    browser.element("#city").click()
    browser.element('#react-select-4-option-1').click()

    # Button
    browser.element('#submit').click()

    # Assertions
    browser.all('tbody td:nth-of-type(2)').should(have.exact_texts(
        'Pinkamena Pie',
        'Cakes_and_bakery@mail.com',
        'Female',
        '9991234567',
        '23 October,2023',
        'Maths',
        'Music',
        'Trixie.jpeg',
        'Sugar Palace, a candy store in Ponyville.',
        'Haryana Panipat'
    ))
