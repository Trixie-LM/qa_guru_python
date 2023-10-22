import os
from selene import be, have, browser


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

class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        browser.should(have.title_containing('DEMOQA'))

    def type_first_name(self, value):
        browser.element('#firstName').type(value)

    def type_last_name(self, value):
        browser.element('#lastName').type(value)

    def type_email(self, value):
        browser.element('#userEmail').type(value)

    def click_gender(self, value):
        browser.element("label[for='gender-radio-2']").click()

    def type_number(self, value):
        browser.element('#userNumber').type(value)
        pass

    def type_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def type_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def click_hobbies(self, value):
        # browser.element('[for="hobbies-checkbox-1"]').click()
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    def download_picture(self, file):
        browser.element("#uploadPicture").send_keys(os.path.abspath('image/Trixie.jpeg'))

    def type_address(self, value):
        browser.element('#currentAddress').type(value)

    def type_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()

    def type_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()

    def click_submit(self, value):
        browser.element(value).click()

    def registered_user_data_should(self, full_name, email, gender, number, date, subject, hobbi, file, address,
                                    state_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name, email, gender, number, date, subject, hobbi, file, address, state_city,
            )
        )