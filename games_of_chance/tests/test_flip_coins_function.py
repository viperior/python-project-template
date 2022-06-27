"""Example test case"""

import logging

import pytest

import games_of_chance.flip_coins


@pytest.mark.parametrize("coin_count", list(range(11)) + list(range(10, 200, 10)) + [1, 2] * 30)
def test_foo_function(coin_count: int) -> None:
    """Example test case

    Parameters:
    coin_count (int): The number of coins to flip

    Returns:
    None
    """
    try:
        coin_flip_result = games_of_chance.flip_coins.flip_coins(coins_to_flip=coin_count,
                                                                 chosen_side="heads")
        logging.debug("coin_flip_result = %s", coin_flip_result)

        assert coin_flip_result["result"] in ["won", "lost", "tie"]
    except AssertionError as error:
        # Validate that trying to flip 0 coins causes an error
        assert isinstance(error, AssertionError) and coin_count == 0
