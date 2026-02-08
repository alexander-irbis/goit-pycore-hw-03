import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """
    Return a sorted list of unique random numbers.

    Parameters:
    - min: minimum possible number in the set (must be >= 1)
    - max: maximum possible number in the set (must be <= 1000)
    - quantity: how many numbers to pick (a value between min and max)

    Returns:
    - list[int]: `quantity` unique random integers in the inclusive range [min, max], sorted ascending
    - []: if any parameter is invalid (wrong type or out of allowed range)
    """

    if (
        not isinstance(min, int)
        or not isinstance(max, int)
        or not isinstance(quantity, int)
        or min < 1
        or max > 1000
        or quantity < min
        or quantity > max
    ):
        return []

    try:
        return sorted(random.sample(range(min, max + 1), quantity))
    except ValueError:
        return []

