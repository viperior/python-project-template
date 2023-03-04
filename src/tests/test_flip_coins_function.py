"""Example test case"""

import logging

import pytest

import src.flip_coins


@pytest.mark.parametrize(
    "coin_flip_count",
    list(range(11)) + list(range(10, 200, 10)) + [1, 2] * 30
)
def test_foo_function(coin_flip_count: int) -> None:
    """Example test case

    Parameters:
    coin_flip_count (int): The number of coins to flip

    Returns:
    None
    """
    try:
        coin_flip_result = src.flip_coins.flip_coins(
            coin_flip_count=coin_flip_count,
            chosen_side="heads"
        )
        logging.debug("coin_flip_result = %s", coin_flip_result)
        assert coin_flip_result["outcome"][0] in ["won", "lost", "tie"]
    except AssertionError as error:
        # Validate that trying to flip 0 coins causes an error
        assert isinstance(error, AssertionError) and coin_flip_count == 0
