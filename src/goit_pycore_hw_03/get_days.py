from datetime import date
import datetime as dt


def get_days_from_date(from_date: date, to_date: date) -> int:
    """
    Calculates the number of days from from_date to to_date (day precision).

    Rules:
    - from_date must be an exact `datetime.date` instance (not `datetime.datetime`, not a subclass)
    - to_date must be an exact `datetime.date` instance (not `datetime.datetime`, not a subclass)

    Why so strict:
    - `datetime.datetime` is a subclass of `datetime.date` and carries time-of-day / timezone semantics.
      Accepting it (even accidentally via `isinstance(x, date)`) widens the function contract and invites
      subtle bugs (DST/timezone/clock issues) if someone later rewrites the implementation using seconds.
    - User-defined subclasses can override behavior; for a small “pure function” we want deterministic,
      built-in date arithmetic only.

    If you have a `datetime`, normalize it before calling:
    - `from_date = from_date.date()`
    - `to_date = to_date.date()`

    Raises:
    - TypeError: if from_date or to_date is not a date

    Returns:
    - int: the number of days from from_date to to_date
    """

    if type(from_date) is not date:
        raise TypeError("from_date must be a date")

    if type(to_date) is not date:
        raise TypeError("to_date must be a date")

    return (to_date - from_date).days

def get_days_from_today(date: str) -> int:
    """
    Calculates the number of days from date to the current date.

    Rules:
    - date must be a string
    - date must be a valid date string in the format YYYY-MM-DD

    Raises:
    - TypeError: if date is not a string
    - ValueError: if date is not a valid date string in the format YYYY-MM-DD

    Returns:
    - int: the number of days from date to the current date
    """

    if not isinstance(date, str):
        raise TypeError("date must be a string")

    try:
        from_date = dt.date.fromisoformat(date)
        result = get_days_from_date(from_date, dt.date.today())
    except ValueError as e:
        raise ValueError(f"date must be in YYYY-MM-DD format and be a real calendar date: {e}") from e

    return result
