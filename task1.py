from datetime import datetime
from typing import Optional


def get_days_from_today(date_str: str) -> Optional[int]:
    """Calculates the number of days between the current date and the date provided by user.

    :param date_str: Date in the format "YYYY-MM-DD"
    :return: The number of days between the current date and the date entered by the user.
    :raises ValueError: If the date is not in the format "YYYY-MM-DD"
    """
    try:
        input_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        today = datetime.today().date()
        difference = (today - input_date).days
        return difference
    except ValueError:
        print(f"Failed to parse date {date_str}. The date must be valid and in following format: 'YYYY-MM-DD'")
        return None


if __name__ == "__main__":
    date = input("Please enter the date in the format 'YYYY-MM-DD': ")
    days = get_days_from_today(date)
    if days is not None:
        print(f"The number of days between today and {date} is {days}.")
