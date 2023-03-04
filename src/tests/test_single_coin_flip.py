"""Test the single coin flip functionality from flip_coins"""

import pytest

import src.flip_coins


def test_single_coin_flip() -> None:
    """Test flipping a single coin"""
    result = src.flip_coins.flip_coin("heads").to_dict()
    assert result["chosen_side"][0] == "heads"
    assert result["result_side"][0] in ["heads", "tails"]
    assert result["outcome"][0] in ["won", "lost"]
    assert result["coin_flip_count"][0] == 1
    assert 0 <= result["heads_count"][0] <= 1
    assert 0 <= result["tails_count"][0] <= 1
    assert result["heads_count"][0] != result["tails_count"][0]
