"""
Copies highlighted text to file based on flag.
Also copies url if copying from Firefox.
Popup is opened to enter a flag.
Todo: add Chromium, cleanup, refactor, validate input
"""
import sys

import get_flag
import get_source
import initialise
import list_fftabs


def write(string):
    """
    Copies string to file.
    :param string:
    :type string:
    """
    source = get_source.get_window()
    if 'Firefox' in source:
        source = source.replace(' \u2014 Mozilla Firefox', '')
        dic = list_fftabs.list_fftabs()
        url = dic.get(source)[0]
    else:
        url = source
    folder_dict = initialise.initialise('/home/sam/Documents/folder/ini')
    flag = get_flag.get_flag()
    if flag in folder_dict:
        with open(folder_dict.get(flag), encoding='utf-8', mode='a') as writer:
            writer.write('\n' + string + '\n' + url + '\n')
    else:
        with open(folder_dict.get('default'), encoding='utf-8', mode='a') as writer:
            writer.write('\n' + string + '\n' + url + '\n')


LINE = ' '.join(sys.argv[1:])
write(LINE)
