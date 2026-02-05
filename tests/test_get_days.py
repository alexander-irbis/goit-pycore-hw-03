from datetime import date, datetime, timedelta

import pytest

from goit_pycore_hw_03 import get_days_from_date, get_days_from_today


@pytest.mark.parametrize(
    ("from_date", "to_date", "expected"),
    [
        (date(2026, 2, 5), date(2026, 2, 5), 0),
        (date(2026, 2, 5), date(2026, 2, 6), 1),
        (date(2026, 2, 6), date(2026, 2, 5), -1),
        # leap year behavior (2024 is a leap year)
        (date(2024, 2, 28), date(2024, 3, 1), 2),
    ],
)
def test_get_days_from_date(from_date: date, to_date: date, expected: int):
    assert get_days_from_date(from_date, to_date) == expected


def test_get_days_from_date_rejects_non_date_inputs():
    with pytest.raises(TypeError, match="from_date must be a date"):
        get_days_from_date("2026-02-05", date(2026, 2, 5))  # type: ignore[arg-type]

    with pytest.raises(TypeError, match="to_date must be a date"):
        get_days_from_date(date(2026, 2, 5), "2026-02-05")  # type: ignore[arg-type]

def test_get_days_from_date_rejects_datetime_and_date_subclasses():
    # `datetime` is a `date` subclass, but the function contract is strict: accept only `date`.
    with pytest.raises(TypeError, match="from_date must be a date"):
        get_days_from_date(datetime(2026, 2, 5, 12, 0, 0), date(2026, 2, 6))

    with pytest.raises(TypeError, match="to_date must be a date"):
        get_days_from_date(date(2026, 2, 5), datetime(2026, 2, 6, 12, 0, 0))

    class MyDate(date):
        pass

    with pytest.raises(TypeError, match="from_date must be a date"):
        get_days_from_date(MyDate(2026, 2, 5), date(2026, 2, 6))

    with pytest.raises(TypeError, match="to_date must be a date"):
        get_days_from_date(date(2026, 2, 5), MyDate(2026, 2, 6))


def test_get_days_from_today_matches_date_today_diff():
    from_date = date(2026, 2, 5)
    expected = (date.today() - from_date).days
    assert get_days_from_today(from_date.isoformat()) == expected


def test_get_days_from_today_is_negative_for_future_date():
    # If the given date is later than the current date, the result must be negative.
    from_date = date.today() + timedelta(days=10)
    assert get_days_from_today(from_date.isoformat()) == -10


@pytest.mark.parametrize(
    "date_str",
    [
        "not-a-date",
        "2026/02/05",
        "2026-02-30",  # impossible date
        "",
    ],
)
def test_get_days_from_today_rejects_invalid_strings(date_str: str):
    with pytest.raises(ValueError, match="date must be in YYYY-MM-DD format"):
        get_days_from_today(date_str)


@pytest.mark.parametrize("value", [123, None, date(2026, 2, 5)])
def test_get_days_from_today_rejects_non_string_inputs(value):
    with pytest.raises(TypeError, match="date must be a string"):
        get_days_from_today(value)  # type: ignore[arg-type]

