"""Test the single coin flip functionality from flip_coins"""

import pytest

import src.flip_coins


def test_single_coin_flip() -> None:
    """Test flipping a single coin"""
    result = src.flip_coins.flip_coin("heads")
    assert result["chosen_side"] == "heads"
    assert result["result_side"] in ["heads", "tails"]
    assert result["outcome"] in ["won", "lost"]
    assert result["coins_flipped"] == 1
    assert 0 <= result["heads_count"] <= 1
    assert 0 <= result["tails_count"] <= 1
    assert result["heads_count"] != result["tails_count"]
