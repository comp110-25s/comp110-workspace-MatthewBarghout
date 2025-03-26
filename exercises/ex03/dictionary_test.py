"""test file for invert, count, favorite_color, bin_len"""

__author__ = 730737376

import pytest
from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


# first use case for invert
def test_invert_usage():
    """Use Case invert with unique key value pairs"""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


# second use case for invert
def test_invert_single_pair():
    """Use Case invert with a single key-value pair"""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


# edge case for invert
def test_invert_duplicate_values():
    """Base Case invert with duplicate values"""
    with pytest.raises(KeyError):
        invert({"kris": "jordan", "michael": "jordan"})


# edge case for count
def test_count_empty_list():
    """Edge case: Tests an empty list."""
    result = count([])
    assert result == {}


# use case for count
def test_count_unique_items():
    """Use case: Tests a list with unique items."""
    result = count(["apple", "banana", "orange"])
    assert result == {
        "apple": 1,
        "banana": 1,
        "orange": 1,
    }


# use case for count
def test_count_repeated_items():
    """Use case: Tests a list with repeated items."""
    result = count(["apple", "banana", "apple", "orange", "banana", "apple"])
    assert result == {
        "apple": 3,
        "banana": 2,
        "orange": 1,
    }


# edge case for favorite color function
def test_favorite_color_edge_case_empty():
    """Edge case: Test with an empty dictionary."""
    result = favorite_color({})
    assert result == ""


# use case for favorite color function
def test_favorite_color_use_case_multiple_colors():
    """Use case: Test with multiple colors where one color is most frequent."""
    result = favorite_color(
        {"Alice": "blue", "Bob": "green", "Charlie": "blue", "David": "red"}
    )
    assert result == "blue"


# use case for favorite color function
def test_favorite_color_use_case_tie_case():
    """Use case: Test with a tie between two colors."""
    result = favorite_color(
        {"Alice": "blue", "Bob": "green", "Charlie": "blue", "David": "green"}
    )
    assert result == "blue"


# use case for bin len
def test_bin_len_case_1():
    """Use Case: Test with strings of various lengths."""
    result = bin_len(["the", "quick", "fox"])
    expected = {3: {"the", "fox"}, 5: {"quick"}}
    assert result == expected, f"Expected {expected}, but got {result}"


# use case for bin len
def test_bin_len_case_2():
    """Use Case: Test with repeated strings."""
    result = bin_len(["the", "the", "fox"])
    expected = {3: {"the", "fox"}}
    assert result == expected, f"Expected {expected}, but got {result}"


# edge case for bin len
def test_bin_len_case_empty():
    """Edge case: Test with an empty list."""
    result = bin_len([])
    expected = {}
    assert result == expected, f"Expected {expected}, but got {result}"
