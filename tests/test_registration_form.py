from data.users import User
from pages.registration_page import RegistrationPage


registration_page = RegistrationPage()


def test_registration_student():
    student = User(
        first_name='Pinkamena',
        last_name='Pie',
        email='Cakes_and_bakery@mail.com',
        gender='Female',
        mobile='9991234567',
        dayofbirth='09',
        mohtofberth='August',
        yearofbirth='2023',
        subject='Maths',
        hobbies='Music',
        picture='Trixie.jpeg',
        address='Sugar Palace, a candy store in Ponyville.',
        state='NCR',
        city='Noida'
    )
    registration_page.open()
    registration_page.register_student(student)
    registration_page.should_have_registered(student)

