"""Return a trigram mutation of an input text file."""

import io
import pprint

def read_file(input_file):
    """Read input file and return list of words in order."""
    f = io.open(input_file, encoding='utf-8')
    text = f.read()
    f.close()
    return text.split()


def create_dict(input_list):
    """Create a dictionary with word pair keys."""
    trigram_dict = {}
    for i in range(len(input_list)-2):
        new_key = input_list[i] + ' ' + input_list[i + 1]
        if new_key not in trigram_dict:
            trigram_dict[new_key] = [input_list[i + 2]]
        else:
            trigram_dict[new_key].append(input_list[i + 2])
    return trigram_dict


if __name__ == '__main__':
    #print (create_dict(read_file('sampletext.txt')))
    #print (read_file('sampletext.txt'))
    dictionary = create_dict(read_file('sampletext.txt'))
    for k, v in dictionary.items():
        print (k,v)


