"""Pytest fixtures"""

import pytest


@pytest.fixture(scope="session")
def fixture_foo():
    """Return an object from fixture_foo"""
    session_object = {
        "foo": "bar",
        "bar": "baz",
    }

    return session_object
