def hello(name: str) -> str:
    """
    Return a friendly greeting for `name`.

    Rules:
    - `name` must be a string
    - leading/trailing whitespace is ignored
    - empty/blank names are rejected
    """

    if not isinstance(name, str):
        raise TypeError("name must be a string")

    normalized = name.strip()
    if not normalized:
        raise ValueError("name must not be empty")

    return f"Hello, {normalized}!"

