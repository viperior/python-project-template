"""Example test case"""

import logging

import foo.foo


def test_foo_function() -> None:
    """Example test case

    Returns:
    None
    """
    coin_flip_result = foo.foo.flip_coins(coins_to_flip=10, chosen_side="heads")
    logging.debug(coin_flip_result)

    assert coin_flip_result["result"] in ["won", "lost", "tie"]
