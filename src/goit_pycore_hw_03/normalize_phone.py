import re

def normalize_phone(phone_number: str) -> str:
    """
    Normalize a phone number to a canonical format used in this homework.

    Note on assumptions:
    - This homework assumes Ukrainian phone-number realities (country code +380).
    - In Ukraine (and in many other countries), domestic phone numbers are often written with a
      leading trunk prefix "0". In international (E.164) format the trunk prefix is not used and
      the number is written with the country code (e.g. +380...).
    - This "leading 0" heuristic is not universal across all regions/countries and may not apply
      to phone numbers outside the intended (Ukrainian) scope of this homework.
    - The assignment text contains: "This guarantees that all numbers will be suitable for sending SMS."
      Based on that, this function is written for the happy path (normalization) and intentionally
      does NOT validate the resulting "international number" against the full standard.
      In production, skipping full validation will lead to guaranteed unpleasant failures.
    """

    pn = '+' if phone_number.startswith("+") else ""
    pn += re.sub(r'\D', '', phone_number)
    if pn.startswith("0"):
        pn = "38" + pn
    if not pn.startswith("+"):
        pn = "+" + pn

    return pn

