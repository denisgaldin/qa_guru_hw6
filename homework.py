from datetime import time


def test_dark_theme_switch():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)
    is_dark_theme = None

    if time(hour=22) <= current_time or current_time < time(hour=6):
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

    current_time = time(hour=16)
    dark_theme_enabled_by_user = True

    is_dark_theme = dark_theme_enabled_by_user or (time(22) <= current_time or current_time < time(6))

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

    # Найдите пользователя с именем "Olga"
    for suitable_users in users:
        if suitable_users['name'] == 'Olga':
            assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suitable_users = []
    for user in users:
        if user['age'] < 20:
            suitable_users.append(user)
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


def print_readable_function_name(func, *args, **kwargs):
    func_name = func.__name__.replace('_', ' ').title()

    arg_list = [str(arg) for arg in args] + [f"{key}={value}" for key, value in kwargs.items()]
    args_string = ", ".join(arg_list)

    result = f"{func_name} [{args_string}]"

    print(result)

    return result


def test_readable_function():
    assert open_browser(browser_name="Chrome") == "Open Browser [Chrome]"
    assert go_to_companyname_homepage(
        page_url="https://companyname.com") == "Go To Companyname Homepage [https://companyname.com]"
    assert find_registration_button_on_login_page(page_url="https://companyname.com/login",
                                                  button_text="Register") == "Find Registration Button On Login Page [https://companyname.com/login, button_text=Register]"


def open_browser(browser_name):
    return print_readable_function_name(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    return print_readable_function_name(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    return print_readable_function_name(find_registration_button_on_login_page, page_url, button_text=button_text)


test_readable_function()
