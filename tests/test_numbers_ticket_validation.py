import pytest

from goit_pycore_hw_03 import get_numbers_ticket


@pytest.mark.parametrize(
    ("min_value", "max_value", "quantity"),
    [
        ("1", 10, 5),
        (1, "10", 5),
        (1, 10, "5"),
    ],
)
def test_get_numbers_ticket_returns_empty_list_for_non_int_inputs(min_value, max_value, quantity):
    assert get_numbers_ticket(min_value, max_value, quantity) == []  # type: ignore[arg-type]


def test_get_numbers_ticket_rejects_min_lt_1():
    assert get_numbers_ticket(0, 10, 5) == []


def test_get_numbers_ticket_rejects_max_gt_1000():
    assert get_numbers_ticket(1, 1001, 5) == []


@pytest.mark.parametrize(
    ("min_value", "max_value", "quantity"),
    [
        (10, 100, 9),
        (10, 100, 101),
    ],
)
def test_get_numbers_ticket_rejects_quantity_outside_min_max(min_value, max_value, quantity):
    assert get_numbers_ticket(min_value, max_value, quantity) == []


def test_get_numbers_ticket_returns_quantity_numbers_for_valid_inputs():
    result = get_numbers_ticket(1, 10, 5)
    assert isinstance(result, list)
    assert len(result) == 5
    assert all(isinstance(x, int) for x in result)
    assert all(1 <= x <= 10 for x in result)
    assert result == sorted(result)
    assert len(set(result)) == len(result)


def test_get_numbers_ticket_has_no_duplicates_across_repeated_calls_dense_case():
    # Domain invariant: the returned sample must not contain duplicate numbers.
    # We repeat the call to increase confidence against buggy "sampling with replacement" implementations.
    for _ in range(50):
        result = get_numbers_ticket(1, 100, 100)
        assert len(result) == 100
        assert result == sorted(result)
        assert all(1 <= x <= 100 for x in result)
        assert len(set(result)) == len(result)

