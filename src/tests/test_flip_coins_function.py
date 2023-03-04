"""Example test case"""

import logging

import pytest

import src.flip_coins


@pytest.mark.parametrize(
    "coin_flip_count",
    list(range(1, 12)) + list(range(10, 200, 10)) + [1, 2] * 30
)
def test_multiple_coin_flips(coin_flip_count: int) -> None:
    """Example test case

    Parameters:
    coin_flip_count (int): The number of coins to flip

    Returns:
    None
    """
    coin_flip_result = src.flip_coins.flip_coins(
        coin_flip_count=coin_flip_count,
        chosen_side="heads"
    )
    logging.debug("coin_flip_result = %s", coin_flip_result)
    assert coin_flip_result["outcome"][0] in ["won", "lost", "tie"]


def test_multiple_coin_flip_invalid_input_type() -> None:
    """Test the exception handling of flip_coins when given an invalid input type"""
    with pytest.raises(TypeError):
        src.flip_coins.flip_coins(
            coin_flip_count="twenty",
            chosen_side="tails",
        )


def test_multiple_coin_flip_zero_times() -> None:
    """Test the exception handling of flip_coins when asked to flip 0 coins"""
    with pytest.raises(ValueError):
        src.flip_coins.flip_coins(
            coin_flip_count=0,
            chosen_side="tails"
        )
