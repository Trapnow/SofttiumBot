import re


def determine_program(q2, q3, q4):
    if q2 == 'да' and q3 == 'математический':
        if q4 == 'да':
            return 'Разработка приложений и программирование на Python'
        return 'Компьютерная графика и web-дизайн'
    elif q2 == 'да' and q3 == 'творческий':
        if q4 == 'нет':
            return 'Компьютерная графика и web-дизайн'
        return 'Создание игр'
    else:
        return 'Базовая компьютерная грамотность'


def validate_email(email: str) -> bool:
    email_regex = re.compile(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    )

    if not email:
        return False

    if not email_regex.match(email):
        return False

    local_part, domain_part = email.split('@')
    if len(local_part) > 64 or len(domain_part) > 253:
        return False

    return True


def validate_phone(phone: str) -> bool:
    cleaned_phone = phone.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')

    pattern = re.compile(
        r'^(?:\+7|8|7)'
        r'(?:\s*\(?\d{3}\)?\s*)'
        r'(?:\s*\d{3}\s*)'
        r'(?:\s*\d{2}\s*)'
        r'(?:\s*\d{2}\s*)$'
    )

    return bool(pattern.match(cleaned_phone))


def validate_class(class_name: str) -> bool:
    pattern = re.compile(
        r'^([1-9]|10|11)'
        r'[a-яА-Я]?$'
    )

    return bool(pattern.match(class_name))
