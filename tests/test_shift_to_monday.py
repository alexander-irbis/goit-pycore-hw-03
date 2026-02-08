from datetime import date

import pytest

from goit_pycore_hw_03.get_upcoming_birthdays import _shift_to_monday


@pytest.mark.parametrize(
    ("input_date", "expected_date"),
    [
        # Weekdays are unchanged (Mon-Fri)
        (date(2026, 2, 9), date(2026, 2, 9)),  # Monday
        (date(2026, 2, 10), date(2026, 2, 10)),  # Tuesday
        (date(2026, 2, 11), date(2026, 2, 11)),  # Wednesday
        (date(2026, 2, 12), date(2026, 2, 12)),  # Thursday
        (date(2026, 2, 13), date(2026, 2, 13)),  # Friday
        # Weekend shifts to Monday
        (date(2026, 2, 14), date(2026, 2, 16)),  # Saturday -> Monday
        (date(2026, 2, 15), date(2026, 2, 16)),  # Sunday -> Monday
    ],
)
def test_shift_to_monday(input_date: date, expected_date: date):
    assert _shift_to_monday(input_date) == expected_date

