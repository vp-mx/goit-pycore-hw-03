import random


def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list[int]:
    """Generates a list of random numbers within the specified range.

    :param min_num: The minimum number in the range. Bigger or equal 1.
    :param max_num: The maximum number in the range. Less or equal 1000.
    :param quantity: The number of random numbers to generate.
    :return: A list of random numbers within the specified range.
    """
    if min_num >= max_num or min_num < 1 or max_num > 1000:
        print("The minimum number must be less than max and both must be in range [1 - 1000].")
        return []
    if quantity > (max_num - min_num + 1):
        print(f"The quantity of numbers must be not more than length of provided range [{min_num}-{max_num}].")
        return []

    numbers = random.sample(range(min_num, max_num + 1), k=quantity)
    return sorted(numbers)


if __name__ == "__main__":
    min_number = int(input("Please enter the minimum number in the range: "))
    max_number = int(input("Please enter the maximum number in the range: "))
    quantity = int(input("Please enter the quantity of numbers to generate: "))
    nums = get_numbers_ticket(min_number, max_number, quantity)
    if nums:
        print(f"Your ticket numbers: {nums}")
