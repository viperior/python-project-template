"""Test the single coin flip functionality from flip_coins"""

import pytest

import src.flip_coins


def test_single_coin_flip() -> None:
    """Test flipping a single coin"""
    result = src.flip_coins.flip_coin("heads")
    assert result["chosen_side"][0] == "heads"
    assert result["result_side"][0] in ["heads", "tails"]
    assert result["outcome"][0] in ["won", "lost"]
    assert result["coin_flip_count"][0] == 1
    assert 0 <= result["heads_count"][0] <= 1
    assert 0 <= result["tails_count"][0] <= 1
    assert result["heads_count"][0] != result["tails_count"][0]


def test_single_coin_flip_invalid_input_type() -> None:
    """Test the exception raising logic when given an invalid input type"""
    with pytest.raises(TypeError):
        src.flip_coins.flip_coin(5)


def test_single_coin_flip_empty_string_value() -> None:
    """Test the exception raising logic when given an empty string value"""
    with pytest.raises(ValueError):
        src.flip_coins.flip_coin("")


def test_single_coin_flip_invalid_string_value() -> None:
    """Test the exception raising logic when given an invalid string value"""
    with pytest.raises(ValueError):
        src.flip_coins.flip_coin("this_is_invalid")
