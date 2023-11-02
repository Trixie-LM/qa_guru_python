from selene import command, have, browser


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.element('label[for="gender-radio-1')
        self.user_mobile = browser.element('#userNumber')
        self.date_of_birth_input = browser.element('#dateOfBirthInput')
        self.date_of_birth_month = browser.element('.react-datepicker__month-select')
        self.date_of_birth_year = browser.element('.react-datepicker__year-select')
        self.subjects_input = browser.element('#subjectsInput')
        self.hobbies = browser.element('//label[. ="Sports"]')
        self.picture = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.state_select = browser.element('#react-select-3-input')
        self.city = browser.element('#city')
        self.city_select = browser.element('#react-select-4-input')
        self.submit = browser.element('#submit')

    def open(self):
        browser.open('/automation-practice-form')
        browser.should(have.title_containing('DEMOQA'))

    def type_first_name(self, value):
        self.first_name.type(value)

    def type_last_name(self, value):
        self.last_name.type(value)

    def type_email(self, value):
        self.email.type(value)

    # TODO: Сделать разветвление
    def click_gender(self, value):
        self.gender.click()

    def type_number(self, value):
        self.user_mobile.type(value)

    # TODO: Проверить
    def type_date_of_birth(self, day, month, year):
        self.date_of_birth_input.click()
        self.date_of_birth_month.type(month)
        self.date_of_birth_year.type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    def type_subjects(self, value):
        self.subjects_input.type(value).press_enter()

    # TODO: Сделать разветвление
    def click_hobbies(self, value):
        # browser.element('[for="hobbies-checkbox-1"]').click()
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    def download_picture(self, file):
        self.picture.send_keys(file)

    def type_address(self, value):
        self.address.type(value)

    def type_state(self, value):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)).click()

    def type_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)).click()

    def click_submit(self):
        self.submit.click()

    def registered_user_data_should(self, full_name, email, gender, number,
                                    date, subject, hobbie, file, address, state_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name, email, gender, number, date, subject, hobbie, file, address, state_city,
            )
        )
