"""Example module flip_coins"""

import logging
import random

import pandas


def flip_coin(chosen_side: str) -> dict:
    """Return the result of a single coin flip given the chosen side

    :param str chosen_side: The player's chosen side ("heads", "tails")
    :return: the result of the single coin flip
    :rtype: dict
    :raises ValueError: if the chosen_side is empty or not "heads" or "tails"
    :raises TypeError: if the chosen_side is not a string

    Example output:
    {
        "chosen_side": "tails",
        "result_side": "heads",
        "outcome": "lost",
        "coins_flipped": 1,
        "heads_count": 1,
        "tails_count": 0,
    }
    """
    # Validate chosen side
    if not isinstance(chosen_side, str):
        raise ValueError("chosen_side must be a string")
    if len(chosen_side) < 1:
        raise ValueError("chosen_side cannot be an empty string")
    if chosen_side not in ["heads", "tails"]:
        raise ValueError(f"The value for chosen_side provided ({chosen_side}) is not an accepted value: heads, tails")
    # Perform the single coin flip
    flip_result = ['heads', 'tails'][random.randrange(0, 2)]
    if flip_result == chosen_side:
        outcome = "won"
    else:
        outcome = "lost"
    heads_count = 0
    tails_count = 0
    if flip_result == "heads":
        heads_count += 1
    else:
        tails_count += 1
    result = {
        "chosen_side": chosen_side,
        "result_side": flip_result,
        "outcome": outcome,
        "coins_flipped": 1,
        "heads_count": heads_count,
        "tails_count": tails_count,
    }
    df = pandas.DataFrame(result, index=[0])
    return df


def flip_coins(coins_to_flip: int, chosen_side: str) -> dict:
    """Flip n coins and reports to the user whether their chosen side, heads or
    tails, won overall.

    Attributes:
    coins_to_flip (int): The number of coins to flip
    chosen_side (str): The coin face chosen by the user to win

    Returns:
    dict: the result of the coin flip(s)

    Example usage:
    flip_data = flip_coins(coins_to_flip=10, chosen_side="tails")

    Example output:
    {
        "chosen_side": "tails"
        "outcome": "won",
        "coins_flipped": 10,
        "heads_count": 4,
        "tails_count": 6
    }
    """
    # Validate input parameters
    assert coins_to_flip > 0

    # Perform the coin flips
    flip_data = [
        0,  # heads
        0   # tails
    ]
    flip_pip_chart = ""
    flip_pip_chart_map = ["H", "T"]

    for index in range(coins_to_flip):
        current_flip = random.randrange(0, 2)
        logging.debug("Flipping coin #%d; result = %d", index, current_flip)
        flip_data[current_flip] += 1
        flip_pip_chart += flip_pip_chart_map[current_flip]

    assert (flip_data[0] + flip_data[1]) == coins_to_flip
    logging.debug(flip_pip_chart)

    # Determine winning face
    if flip_data[0] > flip_data[1]:
        winning_side = "heads"
    elif flip_data[1] > flip_data[0]:
        winning_side = "tails"
    else:
        winning_side = "tie"

    # Determine overall result
    if chosen_side == winning_side:
        overall_result = "won"
    elif winning_side == "tie":
        overall_result = "tie"
    else:
        overall_result = "lost"

    # Return the result
    coin_flip_result = {
        "result": overall_result,
        "coins_flipped": flip_data[0] + flip_data[1],
        "heads_count": flip_data[0],
        "tails_count": flip_data[1]
    }

    # Convert result data to a pandas dataframe
    df = pandas.DataFrame.from_dict(coin_flip_result)

    return df
