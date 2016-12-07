"""Tests for trigrams."""

import pytest

READ_FILE_TABLE = [
    [
        'testtext.txt',
        ['Do', 'the', 'voodoo', 'that', 'you', 'do', 'so', 'well.']
    ]
]


DICT_TABLE = [

        [['Do', 'the', 'voodoo', 'that', 'you', 'do', 'so', 'well.'],
        {'Do the': ['voodoo'], 'the voodoo': ['that'], 'voodoo that': ['you'], 'that you': ['do'], 'you do': ['so'], 'do so': ['well.']}],
        [['Hark!', 'Who', 'goes', 'there?', "'Tis", 'I,', 'some', 'student', 'in', 'Python', '401.', 'Oh.', 'OK,', 'then.', "C'mon", 'in.'],
        {'Hark! Who': ['goes'], 'Who goes': ['there?'], 'goes there?': ["'Tis"], "there? 'Tis": ['I,'], "'Tis I,": ['some'], 'I, some': ['student'], 'some student': ['in'], 'student in': ['Python'], 'in Python': ['401.'], 'Python 401.': ['Oh.'], '401. Oh.': ['OK,'], 'Oh. OK,': ['then.'], 'OK, then.': ["C'mon"], "then. C'mon": ['in.']}]

]


@pytest.mark.parametrize('file, answer', READ_FILE_TABLE)
def test_read_file(file, answer):
    """Test to ensure function is reading text."""
    from trigrams import read_file
    assert read_file(file) == answer


@pytest.mark.parametrize('word_list, result', DICT_TABLE)
def test_create_dict(word_list, result):
    """Test to ensure textfile is read."""
    from trigrams import create_dict
    assert create_dict(word_list) == result
