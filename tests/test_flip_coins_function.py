"""Example test case"""

import logging
import pylint

from games_of_chance.flip_coins import flip_coins


def test_foo_function() -> None:
    """Example test case

    Returns:
    None
    """
    coin_flip_result = flip_coins(coins_to_flip=10, chosen_side="heads")
    logging.debug("coin_flip_result = %s", coin_flip_result)

    assert coin_flip_result["result"] in ["won", "lost", "tie"]
