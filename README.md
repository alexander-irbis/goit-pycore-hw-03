# goit-pycore-hw-03

## Requirements

- Python 3.14+
- Poetry

## Tasks

1. **Task #1: date diff**
   - Implemented in `src/goit_pycore_hw_03/get_days.py`
   - Functions:
     - `get_days_from_date(from_date: datetime.date, to_date: datetime.date) -> int`
     - `get_days_from_today(date: str) -> int`

2. **Task #2: lottery numbers (`get_numbers_ticket`)**
   - Function: `get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]`
   - Parameters:
     - `min` — minimum possible number in the set (>= 1)
     - `max` — maximum possible number in the set (<= 1000)
     - `quantity` — how many numbers to pick (a value between `min` and `max`)
   - Returns:
     - a list of `quantity` unique random integers in the inclusive range `[min, max]`, sorted ascending
     - `[]` on invalid parameters (wrong type or out of allowed range)

3. **Task #3: phone normalization (`normalize_phone`)**
   - Function: `normalize_phone(phone_number: str) -> str`
   - Behavior:
     - keeps only digits, and ensures the result starts with a single leading `+`
     - determines whether the input is in international form by checking for a leading `+` in the raw input
     - if the raw input does **not** start with `+` (no leading `+`):
       - if the cleaned number starts with the domestic trunk prefix `0`, the function prepends `38` (Ukraine assumption) so it becomes `380...`
     - finally, if the normalized number does not start with `+`, the function prepends `+`
   - Note:
     - per the assignment statement ("This guarantees that all numbers will be suitable for sending SMS"),
       this is treated as a happy-path normalization task; the resulting “international number” is not
       validated against the full standard (in production, skipping full validation will cause failures)
     - Murphy’s law (practical reminder): "If anything can go wrong, it will."

4. **Task #4: upcoming birthdays (`get_upcoming_birthdays`)**
   - Function: `get_upcoming_birthdays(users: list[dict[str, str]], as_of_date: date | None = None) -> list[dict[str, str]]`
   - Input (`users`): list of dicts, each item has:
     - `name` — `str`
     - `birthday` — `str` in `YYYY.MM.DD` format
   - Output: list of dicts, each item has:
     - `name` — `str`
     - `congratulation_date` — `str` in `YYYY.MM.DD` format
   - Behavior:
     - selects users whose birthday occurrence date is within the next **7 days**, including today:
       - window semantics: `[as_of_date, as_of_date + 7 days)` (half-open; excludes exactly `+7` days to avoid weekly overlap)
     - if a selected birthday falls on Saturday/Sunday, shifts `congratulation_date` to the nearest Monday
     - leap-day policy: birthdays on Feb 29 are celebrated on Mar 1 in non-leap years

## Quick start

```bash
poetry install
poetry run pytest
```

## Project layout

- `src/goit_pycore_hw_03/` — package code
- `tests/` — tests

