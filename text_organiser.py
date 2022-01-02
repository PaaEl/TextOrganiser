"""
Copies lines which have a flag \\xy at the beginning of them from a master file.
Copy location depends on xy, can be set in ini file.
Creates an additional textfile in the master directory to keep track of copied lines.
Todo: cleanup, refactor, validate input
"""
import os
from itertools import islice

import initialise


def organise(f='/home/sam/Documents/test/master', e='utf-8'):
    """
    Sets a default file and encoding.
    :param e:
    :param f:
    """
    file = f
    encoding = e
    read(file, encoding)


def read(file, encoding):
    """
    Reads the file, checks for flagged lines.
    Keeps track of the line we're on in a helper document "linenumber".
    :param file:
    :param encoding:
    """
    folder_dict = initialise.initialise()
    print(folder_dict)
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(file)), 'linenumber')):
        with open(os.path.join(os.path.dirname(os.path.abspath(file)), 'linenumber'),
                  encoding=encoding, mode='r') as number:
            x = int(number.readline())
    else:
        x = 0
    with open(file, encoding=encoding, mode='r+') as reader:
        line_number = 0
        f = islice(reader, x, None)
        for line in f:
            line_number += 1
            print(line)
            if line[0] == '\\':
                if folder_dict.get(line[1:3]) is not None:
                    write(folder_dict.get(line[1:3]), encoding, line)
                else:
                    try:
                        write(folder_dict.get('default_folder'),
                              encoding, line)
                    except OSError:
                        print('Couldn\'t write flag to file.')

        x += line_number
    with open(os.path.join(os.path.dirname(os.path.abspath(file)), 'linenumber'),
              encoding=encoding, mode='w') as number:
        number.write(str(x))


def write(file, encoding, line):
    """
    Writes the lines to their target files.
    :param file:
    :param encoding:
    :param line:
    """
    with open(file, encoding=encoding, mode='a') as writer:
        writer.write('\n' + line)


organise()
