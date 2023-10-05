from datetime import time


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    start_time = time(hour=22)
    end_time = time(hour=6)
    current_time = time(hour=23)
    is_dark_theme = None

    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)
    if start_time <= current_time or current_time < end_time:
        is_dark_theme = True
    else:
        is_dark_theme = False

    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    start_time = time(hour=22)
    end_time = time(hour=6)
    current_time = time(hour=22)
    dark_theme_enabled_by_user = True
    is_dark_theme = None

    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную

    if dark_theme_enabled_by_user:
        is_dark_theme = True
    elif dark_theme_enabled_by_user is False:
        is_dark_theme = False
    elif start_time <= current_time or current_time < end_time:
        is_dark_theme = True
    else:
        is_dark_theme = False

    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    # Вариант 1
    suitable_users = [user for user in users if user["name"] == 'Olga'][0]
    assert suitable_users == {"name": "Olga", "age": 45}

    # Вариант 2
    index = 0
    for i, value in enumerate(users):
        if value["name"] == 'Olga':
            index = i
            break
    suitable_users = users[index]
    assert suitable_users == {"name": "Olga", "age": 45}

    # Вариант 3
    def filter_odd_num(dict):
        if dict["name"] == "Olga":
            return True

    suitable_users = list(filter(filter_odd_num, users))[0]
    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    # Вариант 1
    users.sort(key=lambda user: user['age'])
    for index, value in enumerate(users):
        if value["age"] > 20:
            suitable_users = users[0:index]
            break

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]

    # Вариант 2
    suitable_users = [user for user in users if user["age"] < 20]
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def get_name_function_and_args(function, *args):
    function_name = function.__name__.replace('_', ' ').title()
    arguments = ', '.join(args)
    result = f"{function_name} [{arguments}]"
    print(result)
    return result

def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = get_name_function_and_args(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = get_name_function_and_args(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = get_name_function_and_args(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"


