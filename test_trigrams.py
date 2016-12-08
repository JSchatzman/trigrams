"""Test trigrams module for reading, splitting and output file."""

import pytest


DICT_TABLE = [

    ['testtext.txt',
        {
            'Do the': ['voodoo'],
            'the voodoo': ['that'],
            'voodoo that': ['you'],
            'that you': ['do'],
            'you do': ['so'],
            'do so': ['well.']
        }],

    ['dict_testtext.txt',
        {
            'Hark! Who': ['goes'],
            'Who goes': ['there?'],
            'goes there?': ["'Tis"],
            "there? 'Tis": ['I,'],
            "'Tis I,": ['some'],
            'I, some': ['student'],
            'some student': ['in'],
            'student in': ['Python'],
            'in Python': ['401.'],
            'Python 401.': ['Oh.'],
            '401. Oh.': ['OK,'],
            'Oh. OK,': ['then.'],
            'OK, then.': ["C'mon"],
            "then. C'mon": ['in.']}]
]


def test_read_file():
    """Test to ensure read_file function is reading text."""
    from trigrams import read_file
    assert read_file('testtext.txt') == [
        'Do', 'the', 'voodoo', 'that', 'you', 'do', 'so', 'well.'
    ]


@pytest.mark.parametrize('word_list, result', DICT_TABLE)
def test_create_dict(word_list, result):
    """Check create_dict is populating a dictionary from sample text."""
    from trigrams import create_dict
    assert create_dict(word_list) == result


# @pytest.mark.parametrize('word_list, result', DICT_TABLE)
def test_main():
    """Test to ensure main function is producing correct length text."""
    from trigrams import main
    output = main('rando.txt', 200)
    assert len(output.split()) == 200
