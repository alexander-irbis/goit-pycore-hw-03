from datetime import date

from goit_pycore_hw_03 import get_upcoming_birthdays


def _by_name(items: list[dict[str, str]]) -> list[dict[str, str]]:
    return sorted(items, key=lambda x: x["name"])


def test_empty_input_returns_empty_list():
    assert get_upcoming_birthdays([], as_of_date=date(2026, 2, 6)) == []

def test_includes_today_and_next_7_days_inclusive_and_shifts_weekends_to_monday():
    # 2026-02-06 is Friday. The 7-day window is half-open: includes today through +6 days.
    as_of = date(2026, 2, 6)
    users = [
        {"name": "Alice", "birthday": "1990.02.06"},  # today (Fri) -> Fri
        {"name": "Bob", "birthday": "1991.02.07"},  # Sat -> Mon
        {"name": "Carol", "birthday": "1992.02.08"},  # Sun -> Mon
        {"name": "Dave", "birthday": "1993.02.13"},  # exactly +7 days -> excluded (half-open window)
        {"name": "Eve", "birthday": "1994.02.14"},  # +8 days -> excluded
    ]

    expected = _by_name(
        [
            {"name": "Alice", "congratulation_date": "2026.02.06"},
            {"name": "Bob", "congratulation_date": "2026.02.09"},
            {"name": "Carol", "congratulation_date": "2026.02.09"},
        ]
    )

    assert _by_name(get_upcoming_birthdays(users, as_of_date=as_of)) == expected


def test_window_can_cross_year_boundary_and_weekend_shift_can_move_into_next_year():
    # 2026-12-28 is Monday. The 7-day window includes through 2027-01-03 (Sunday).
    # Note: congratulation_date can be shifted to Monday 2027-01-04 even if it lies outside the window,
    # because the window applies to the birthday date, not the shifted congratulation date.
    as_of = date(2026, 12, 28)
    users = [
        {"name": "Alice", "birthday": "1990.12.28"},  # today
        {"name": "Bob", "birthday": "1991.12.31"},  # Thu
        {"name": "Carol", "birthday": "1992.01.01"},  # Fri (next year)
        {"name": "Dave", "birthday": "1993.01.03"},  # Sun (next year) -> Mon 2027-01-04
    ]

    expected = _by_name(
        [
            {"name": "Alice", "congratulation_date": "2026.12.28"},
            {"name": "Bob", "congratulation_date": "2026.12.31"},
            {"name": "Carol", "congratulation_date": "2027.01.01"},
            {"name": "Dave", "congratulation_date": "2027.01.04"},
        ]
    )

    assert _by_name(get_upcoming_birthdays(users, as_of_date=as_of)) == expected


def test_leap_day_birthdays_are_celebrated_on_march_1_in_non_leap_years_and_shifted_if_weekend():
    # 2025 is not a leap year; 2025-03-01 is Saturday -> shift to Monday 2025-03-03.
    as_of = date(2025, 2, 25)  # Tuesday
    users = [
        {"name": "Leap", "birthday": "1992.02.29"},
    ]

    assert get_upcoming_birthdays(users, as_of_date=as_of) == [
        {"name": "Leap", "congratulation_date": "2025.03.03"}
    ]


def test_leap_day_birthdays_use_feb_29_in_leap_years():
    # 2024 is a leap year; 2024-02-29 is Thursday -> no shift.
    as_of = date(2024, 2, 25)  # Sunday
    users = [
        {"name": "Leap", "birthday": "1992.02.29"},
    ]

    assert get_upcoming_birthdays(users, as_of_date=as_of) == [
        {"name": "Leap", "congratulation_date": "2024.02.29"}
    ]

