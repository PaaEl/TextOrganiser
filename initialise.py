"""
Creates dictionary to assign flags to target files.
Todo: cleanup, refactor
"""
import configparser


def initialise(file='/home/sam/Documents/test/ini', encoding='utf-8'):
    """
    Creates dictionary to assign flags to target files.
    :rtype: dictionary
    :param file:
    :param encoding:
    """
    folder_dict = {}
    config = configparser.ConfigParser()
    with open(file, encoding=encoding) as reader:
        config.read_file(reader)
        for k, v in config.items('folder'):
            folder_dict[k] = v
    return folder_dict
