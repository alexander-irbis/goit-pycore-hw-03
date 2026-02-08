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

## Quick start

```bash
poetry install
poetry run pytest
```

## Project layout

- `src/goit_pycore_hw_03/` — package code
- `tests/` — tests

