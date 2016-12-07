"""Tests for trigrams."""

import pytest

READ_EVAL_TABLE = [
    ['testtext.txt', ['Do', 'the', 'voodoo', 'that', 'you', 'do', 'so', 'well.']]
]


@pytest.mark.parametrize('file, answer', READ_EVAL_TABLE)
def test_read_file(file, answer):
    """Test to ensure function is reading text."""
    from trigrams import read_file
    assert read_file(file) == answer


# @pytest.mark.parametrize('str, n, result', READ_EVAL_TABLE)
# def test_read_eval(str, n, result):
#     """Test to ensure textfile is read."""
#     from trigrams import read_file
#     assert read_file(str, n) == result
