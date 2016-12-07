"""Return a trigram mutation of an input text file."""

import io


def read_file(input_file):
    """Read input file and return list of words in order."""
    f = io.open(input_file, encoding='utf-8')
    text = f.read()
    f.close()
    return text.split()


if __name__ == '__main__':
    print (read_file('sampletext.txt'))
