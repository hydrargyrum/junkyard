#!/usr/bin/env python3
# SPDX-License-Identifier: WTFPL
# convert a `stat()` file mode to a string like "-rwxr-xr-x"

import stat


MODE_TYPES = {
    stat.S_ISREG: "-",
    stat.S_ISDIR: "d",
    stat.S_ISLNK: "l",
    stat.S_ISBLK: "b",
    stat.S_ISCHR: "c",
    stat.S_ISSOCK: "s",
    stat.S_ISFIFO: "p",
}


def _perm_part(
    perms: int, r: int, w: int, x: int, special, special_letter: str
) -> str:
    result = list("---")
    if perms & r:
        result[0] = "r"
    if perms & w:
        result[1] = "w"
    if perms & special:
        if perms & x:
            result[2] = special_letter
        else:
            result[2] = special_letter.upper()
    elif perms & x:
        result[2] = "x"
    return "".join(result)


def mode_to_string(mode: int) -> str:
    result = list("?---------")
    perms = stat.S_IMODE(mode)
    for func in MODE_TYPES:
        if func(mode):
            result[0] = MODE_TYPES[func]
            break

    result[1:4] = _perm_part(
        perms, stat.S_IRUSR, stat.S_IWUSR, stat.S_IXUSR, stat.S_ISUID, "s",
    )
    result[4:7] = _perm_part(
        perms, stat.S_IRGRP, stat.S_IWGRP, stat.S_IXGRP, stat.S_ISGID, "s",
    )
    result[7:10] = _perm_part(
        perms, stat.S_IROTH, stat.S_IWOTH, stat.S_IXOTH, stat.S_ISVTX, "t",
    )

    return "".join(result)


# unit tests

def test_mode_to_string():
    assert mode_to_string(0o000777) == "?rwxrwxrwx"
    assert mode_to_string(0o100653) == "-rw-r-x-wx"
    assert mode_to_string(0o047000) == "d--S--S--T"
    assert mode_to_string(0o017111) == "p--s--s--t"
