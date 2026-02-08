"""GoIT PyCore homework #03."""

from .get_days import get_days_from_date, get_days_from_today
from .get_upcoming_birthdays import get_upcoming_birthdays
from .hello import hello
from .numbers_ticket import get_numbers_ticket
from .normalize_phone import normalize_phone

__version__ = "0.1.0"

__all__ = [
    "__version__",
    "hello",
    "get_days_from_date",
    "get_days_from_today",
    "get_upcoming_birthdays",
    "get_numbers_ticket",
    "normalize_phone",
]
