"""Example module flip_coins"""

import logging
import random

import pandas


def flip_coin(chosen_side: str) -> pandas.DataFrame:
    """Return the result of a single coin flip given the chosen side

    :param str chosen_side: The player's chosen side ("heads", "tails")
    :return: the result of the single coin flip in a dataframe
    :rtype: pandas.DataFrame
    :raises ValueError: if the chosen_side is empty or not "heads" or "tails"
    :raises TypeError: if the chosen_side is not a string

    Example output:
    {
        "chosen_side": "tails",
        "result_side": "heads",
        "outcome": "lost",
        "coin_flip_count": 1,
        "heads_count": 1,
        "tails_count": 0,
    }
    """
    # Validate chosen side
    if not isinstance(chosen_side, str):
        raise TypeError("chosen_side must be a string")
    if len(chosen_side) < 1:
        raise ValueError("chosen_side cannot be an empty string")
    if chosen_side not in ["heads", "tails"]:
        error_message = (
            f"The value for chosen_side provided ({chosen_side}) "
            f"is not an accepted value: heads, tails"
        )
        raise ValueError(error_message)
    # Perform the single coin flip
    flip_result = ['heads', 'tails'][random.randrange(0, 2)]
    win_count = 0
    loss_count = 0
    if flip_result == chosen_side:
        outcome = "won"
        win_count += 1
    else:
        outcome = "lost"
        loss_count += 1
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
        "coin_flip_count": 1,
        "heads_count": heads_count,
        "tails_count": tails_count,
    }
    df = pandas.DataFrame(result, index=[0])
    return df


def flip_coins(coin_flip_count: int, chosen_side: str) -> dict:
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
        "chosen_side": "tails",
        "winning_side": "tails",
        "outcome": "won",
        "coin_flip_count": 10,
        "heads_count": 4,
        "tails_count": 6,
    }
    """
    # Validate input parameters
    if not isinstance(coin_flip_count, int):
        raise TypeError('The number of coins must be an integer')
    if coin_flip_count < 1:
        raise ValueError('The number of coins must be an positive, non-zero integer')

    # Perform the coin flips
    flip_dataframes = []  # List of dataframes from single flips
    for index in range(coin_flip_count):
        current_flip = flip_coin(chosen_side)
        logging.debug("Flipped coin #%d; result = \n%s", index, current_flip)
        flip_dataframes.append(current_flip)
    flip_data = pandas.concat(flip_dataframes)

    # Determine winning face
    if sum(flip_data["heads_count"]) > sum(flip_data["tails_count"]):
        winning_side = "heads"
    elif sum(flip_data["heads_count"]) < sum(flip_data["tails_count"]):
        winning_side = "tails"
    else:
        winning_side = "tie"

    # Determine overall outcome
    if chosen_side == winning_side:
        outcome = "won"
    elif winning_side == "tie":
        outcome = "tie"
    else:
        outcome = "lost"

    # Return the result
    result = {
        "chosen_side": chosen_side,
        "winning_side": winning_side,
        "outcome": outcome,
        "coin_flip_count": sum(flip_data["coin_flip_count"]),
        "heads_count": sum(flip_data["heads_count"]),
        "tails_count": sum(flip_data["tails_count"]),
    }

    # Convert result data to a pandas dataframe
    df = pandas.DataFrame(result, index=[0])

    return df
