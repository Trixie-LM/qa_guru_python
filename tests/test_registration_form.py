from pages.registration_page import RegistrationPage
from pathlib import Path
import allure

registration_page = RegistrationPage()


@allure.title("Successful fill form")
def test_registration_form():

    with allure.step('Open registrations form'):
        registration_page.open()

    with allure.step('Fill form'):
        registration_page.type_first_name('Pinkamena')
        registration_page.type_last_name('Pie')
        registration_page.type_email('Cakes_and_bakery@mail.com')
        registration_page.click_gender('male')
        registration_page.type_number('9991234567')
        registration_page.type_date_of_birth('23', 'August', '2023')
        registration_page.type_subjects('Maths')
        registration_page.click_hobbies('Music')
        registration_page.download_picture(str(Path(__file__).parent.joinpath(f'image/Trixie.jpeg')))
        registration_page.type_address('Sugar Palace, a candy store in Ponyville.')
        registration_page.type_state('NCR')
        registration_page.type_city('Noida')
        registration_page.click_submit()

    with allure.step("Check form results"):
        registration_page.registered_user_data_should(
            'Pinkamena Pie',
            'Cakes_and_bakery@mail.com',
            'Male',
            '9991234567',
            '23 August,2023',
            'Maths',
            'Music',
            'Trixie.jpeg',
            'Sugar Palace, a candy store in Ponyville.',
            'NCR Noida'
        )
