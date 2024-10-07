from datetime import datetime, timedelta


def get_upcoming_birthdays(users_list: list[dict[str, str]]) -> list[dict[str, str]]:
    """Returns a list of upcoming birthdays within the next 7 days.

    When the birthday falls on a weekend, the congratulation date is moved to the next week.

    :param users_list: A list of dictionaries with user data. Each dictionary must contain 'name' and 'birthday' keys.
    :return: A list of dictionaries with names and dates to congratulate.
    Example ::

     [{'user': 'John Doe', 'congratulation_date': '2024.10.14'}]
    """
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users_list:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        greet_date = birthday.replace(year=today.year)

        if greet_date < today:
            greet_date = greet_date.replace(year=today.year + 1)

        days_until_greet = greet_date - today
        if days_until_greet.days <= 7:
            if greet_date.isoweekday() in (6, 7):
                greet_date += timedelta(days=8 - greet_date.isoweekday())  # Move to the next week
            congratulation_date = greet_date.strftime("%Y.%m.%d")
            upcoming_birthdays.append({"user": user["name"], "congratulation_date": congratulation_date})

    return upcoming_birthdays


if __name__ == "__main__":
    users = [
        {"name": "John Doe0", "birthday": "1983.12.28"},
        {"name": "John Doe1", "birthday": "1983.01.02"},
        {"name": "John Doe2", "birthday": "1983.01.06"},
        {"name": "John Doe3", "birthday": "1978.10.06"},
        {"name": "John Doe4", "birthday": "2000.10.07"},
        {"name": "Jane Doe5", "birthday": "1987.10.12"},
        {"name": "John Smith", "birthday": "2001.10.13"},
        {"name": "Jane Smith", "birthday": "1982.10.14"},
        {"name": "John Johnson", "birthday": "1965.10.15"},
    ]

    upcoming = get_upcoming_birthdays(users)
    print("Upcoming birthdays within the next 7 days:")
    for user_to_greet in upcoming:
        print(f"Congratulations to {user_to_greet['user']} on {user_to_greet['congratulation_date']}!")
