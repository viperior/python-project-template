"""Example module flip_coins"""

import logging
import random

import pandas


def flip_coins(coins_to_flip: int, chosen_side: str) -> dict:
    """Flip n coins and reports to the user whether their chosen side, heads or
    tails, won overall.

    Attributes:
    coins_to_flip (int): The number of coins to flip
    chosen_side (str): The coin face chosen by the user to win

    Returns:
    dict: the result of the coin flip(s)

    Example call:

    ``` python
    flip_data = flip_coins(coins_to_flip=10, chosen_side="tails")
    ```

    Example output:

    ``` python
    {
        "result": "won",
        "coins_flipped": 10,
        "heads_count": 4,
        "tails_count": 6
    }
    ```
    """
    # Validate input parameters
    assert coins_to_flip > 0
    assert len(chosen_side) > 0
    assert chosen_side in ["heads", "tails"]

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
