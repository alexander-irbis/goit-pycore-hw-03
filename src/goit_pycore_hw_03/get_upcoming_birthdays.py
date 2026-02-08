from datetime import date, datetime, timedelta


def get_upcoming_birthdays(
    users: list[dict[str, str]],
    as_of_date: date | None = None,
) -> list[dict[str, str]]:
    """
    Find upcoming birthdays and assign congratulations dates.

    Input:
    - users: list[dict] with elements:
      - name: str
      - birthday: str in 'YYYY.MM.DD' format
    - as_of_date (optional): date to calculate from (datetime.date)
      - if omitted, the function uses the current date (date.today())

    Output:
    - list[dict] with elements:
      - name: str
      - congratulation_date: str in 'YYYY.MM.DD' format

    Behavior:
    - finds all users whose birthdays fall within a 7-day window starting today (including today)
      - window semantics: [as_of_date, as_of_date + 7 days) (half-open; excludes exactly +7 days)
      - rationale: if a script runs weekly, a closed interval would overlap at the boundary and cause duplicates
    - determines the nearest working day and assigns it as the congratulation date

    Assumptions:
    - there are two weekend days: Saturday and Sunday
    - there are no holidays or vacations; therefore the nearest working day after the weekend is always Monday
    - leap-day policy: birthdays on Feb 29 are celebrated on Mar 1 in non-leap years
    """

    if as_of_date is None:
        as_of_date = date.today()

    if type(as_of_date) is not date:
        raise TypeError("as_of_date must be a date object")

    year = as_of_date.year
    next_year = year + 1

    window_length = 7  # length of the window in days (half-open: [today, today+7days))

    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # get the birthday for the current year
        congratulation_date = _birthday_for_year(birthday, year)

        # if the birthday is in the past, use the next year
        if congratulation_date < as_of_date:
            congratulation_date = _birthday_for_year(birthday, next_year)

        # if the birthday is within the window, add it to the list
        if as_of_date + timedelta(days=window_length) > congratulation_date:
            # shift the birthday to the nearest Monday
            congratulation_date = _shift_to_monday(congratulation_date)
            # add the congratulation date to the list
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
            })

    return upcoming_birthdays


def _birthday_for_year(birthday: date, year: int) -> date:
    """
    Return the birthday occurrence date for a specific year.
    If the birthday is Feb 29 and the year is not leap, use Mar 1.
    """
    try:
        return birthday.replace(year=year)
    except ValueError:
        if birthday.month == 2 and birthday.day == 29:
            return birthday.replace(year=year, month=3, day=1)
        raise


def _shift_to_monday(d: date) -> date:
    """
    Shift a date to the nearest Monday.
    - if the date is a Saturday, shift it to the next Monday
    - if the date is a Sunday, shift it to the next Monday
    - otherwise, return the date as is
    """
    if d.weekday() == 5:
        # Saturday
        return d + timedelta(days=2)
    elif d.weekday() == 6:
        # Sunday
        return d + timedelta(days=1)
    else:
        return d
