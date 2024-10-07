import re


def normalize_phone(phone_number: str) -> str:
    """Normalizes valid ukrainian phone number to the international format.

    :param phone_number: String with valid ukrainian phone number in any format.
    :return: Normalized to international format phone number. e.g. +380441234567.
    """
    clean_number = re.sub(r"\D", "", phone_number)
    return f"+380{clean_number[-9:]}"


if __name__ == "__main__":
    raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
