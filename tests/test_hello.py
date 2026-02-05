import pytest

from goit_pycore_hw_03 import hello


def test_hello_simple():
    assert hello("Alice") == "Hello, Alice!"


def test_hello_strips_whitespace():
    assert hello("  Alice \n") == "Hello, Alice!"


def test_hello_rejects_blank_name():
    with pytest.raises(ValueError, match="must not be empty"):
        hello("   ")


def test_hello_rejects_non_string():
    with pytest.raises(TypeError, match="must be a string"):
        hello(123)  # type: ignore[arg-type]

