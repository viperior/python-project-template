"""Example usage of a pytest fixture"""

import logging


def test_fixture_usage_examples(fixture_foo) -> None:
    """Example usage of a pytest fixture"""
    assert isinstance(fixture_foo, dict)
    assert len(fixture_foo) > 0
    logging.info("Logging info message = %s", fixture_foo["foo"])
    fixture_foo["new"] = "new foo"
    assert "new" in fixture_foo.keys()
    assert fixture_foo["new"] == "new foo"
