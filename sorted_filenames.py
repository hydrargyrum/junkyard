#!/usr/bin/python3
# SPDX-License-Identifier: WTFPL

import locale
import pathlib
import unicodedata


def file_key(path):
    # sort using locale params, not using pure Unicode codepoint number
    name = path.name
    name = unicodedata.normalize(name, "NFKD")
    name = locale.strxfrm(name)

    # could detect numbers in filenames and use them for sort?
    # see https://gitlab.com/hydrargyrum/attic/-/tree/master/sort-with-numbers

    # sort directories first?
    # dir_first = -int(path.is_dir())
    # return (dir_first, name)

    return name


locale.setlocale(locale.LC_ALL, "")

files = pathlib.Path().iterdir()
files = sorted(files, key=file_key)
print(*files, sep="\n")
