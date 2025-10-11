import random

def get_numbers_ticket(min_value: int, max_value: int, quantity: int) -> list[int]:
    """
    Generates a sorted list of unique random numbers for a lottery ticket.
    """

    if (
            not (1 <= min_value <= 1000) or
            not (1 <= max_value <= 1000) or
            min_value > max_value or
            quantity <= 0 or
            quantity > (max_value - min_value + 1)
    ):
        return []

    numbers = random.sample(range(min_value, max_value + 1), quantity)

    return sorted(numbers)