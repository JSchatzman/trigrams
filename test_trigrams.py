"""Tests for trigrams."""

import pytest

READ_EVAL_TABLE = [
    ["I may I wish I may I wish I might", 3, ["I", "wish", "may"]],
    ["Do that voodoo that you do so well.", 4, ["voodoo", "that", "you", "do"]]
]


@pytest.mark.parametrize('str, answer')
def test_read_file(str):
    """Test to ensure function is reading text."""
    from trigrams import read_file
    assert read_file("This is a string") == ["this", "is", "a", "string"]


@pytest.mark.parametrize('str, n, result', READ_EVAL_TABLE)
def test_read_eval(str, n, result):
    """Test to ensure textfile is read."""
    from trigrams import read_file
    assert read_file(str, n) == result
