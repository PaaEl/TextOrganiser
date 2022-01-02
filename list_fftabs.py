"""
List all Firefox tabs with title and URL

Supported input: json or jsonlz4 recovery files
Default output: title (URL)
Output format can be specified as argument
from https://gist.github.com/tmonjalo/33c4402b0d35f1233020bf427b5539fa
"""

import json
import pathlib

import lz4.block


def list_fftabs():
    path = pathlib.Path.home().joinpath('.mozilla/firefox')
    files = path.glob('*default*/sessionstore-backups/recovery.jsonlz4')
    dic = {}
    for f in files:
        b = f.read_bytes()
        if b[:8] == b'mozLz40\0':
            b = lz4.block.decompress(b[8:])
        j = json.loads(b)
        for w in j['windows']:
            for t in w['tabs']:
                i = t['index'] - 1
                dic[t['entries'][i]['title']] = [t['entries'][i]['url']]
    return dic
