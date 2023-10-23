import os

from selene.support.shared import browser
from selene import be, have

from pages.registration_page import RegistrationPage


registration_page = RegistrationPage()


def test_registration_form():

    registration_page.open()
    registration_page.type_first_name('Pinkamena')
    registration_page.type_last_name('Pie')
    registration_page.type_email('Cakes_and_bakery@mail.com')
    registration_page.click_gender()
    registration_page.type_number('9991234567')
    registration_page.type_date_of_birth('1', 'September', '2000')
    registration_page.type_subjects('Maths')
    registration_page.click_hobbies()
    registration_page.download_picture(os.path.abspath('image/Trixie.jpeg'))
    registration_page.type_address('Sugar Palace, a candy store in Ponyville.')
    registration_page.type_state('NCR')
    registration_page.type_city('Noida')
    registration_page.click_submit()

    registration_page.registered_user_data_should(
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
    )
