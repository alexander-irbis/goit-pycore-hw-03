from datetime import date

import pytest

from goit_pycore_hw_03.get_upcoming_birthdays import _birthday_for_year


def test_birthday_for_year_regular_date_changes_only_year():
    birthday = date(1990, 6, 15)
    assert _birthday_for_year(birthday, 2026) == date(2026, 6, 15)


@pytest.mark.parametrize(
    ("target_year", "expected"),
    [
        (2024, date(2024, 2, 29)),  # leap year keeps Feb 29
        (2025, date(2025, 3, 1)),  # non-leap year maps Feb 29 -> Mar 1
        (2100, date(2100, 3, 1)),  # 2100 is not leap (century rule)
        (2000, date(2000, 2, 29)),  # 2000 is leap (century exception)
    ],
)
def test_birthday_for_year_leap_day_policy(target_year: int, expected: date):
    birthday = date(1992, 2, 29)
    assert _birthday_for_year(birthday, target_year) == expected


def test_birthday_for_year_does_not_mutate_original_date():
    birthday = date(1992, 2, 29)
    _ = _birthday_for_year(birthday, 2025)
    assert birthday == date(1992, 2, 29)

