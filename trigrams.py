"""Return a trigram mutation of an input text file."""

from __future__ import unicode_literals
import io
import random


def read_file(input_file):
    """Read input file and return list of words in order."""
    f = io.open(input_file, encoding='utf-8')
    text = f.read()
    f.close()
    return text.split()


def create_dict(input_file):
    """Create a dictionary with word pair keys."""
    input_list = read_file(input_file)
    trigram_dict = {}
    for i in range(len(input_list) - 2):
        new_key = input_list[i] + ' ' + input_list[i + 1]
        if new_key not in trigram_dict:
            trigram_dict[new_key] = [input_list[i + 2]]
        else:
            trigram_dict[new_key].append(input_list[i + 2])
    return trigram_dict


def main(input_file, word_length):
    """Output the trigram based using the input dictionary of lists."""
    trigram_dict = create_dict(input_file)
    output = []
    word_pair_list = list(trigram_dict.keys())
    word_pair = random.choice(word_pair_list)
    output.extend(word_pair.split(' '))
    third_word = random.choice(trigram_dict[word_pair])
    word_pair = ' '.join(output[-2:])
    while len(output) < word_length + 3:
        if word_pair in word_pair_list:
            third_word = random.choice(trigram_dict[word_pair])
            output.append(third_word)
            word_pair = ' '.join(output[-2:])
        else:
            word_pair = random.choice(word_pair_list)
    return ' '.join(output[0:word_length])


if __name__ == '__main__':
    print (main('sampletext.txt', 50))
