# SPDX-License-Identifier: WTFPL

import sys

# standard lib's fileinput module can't handle null-separated "lines"
# because of https://github.com/python/cpython/issues/94615
# this would be useful for implementing `--zero`-like command-line flags

# so here's an attempt at doing so


def fileinput_sep(files=None, *, linesep="\n", openhook=None):
    if files is None:
        files = sys.argv[1:]
    if not files:
        files = ("-",)

    for file in files:
        if file == "-":
            fp = sys.stdin
        else:
            if openhook:
                fp = openhook(file)
            else:
                fp = open(file, "r")

        with fp:
            yield from iter_lines(fp, linesep=linesep)


def iter_lines(fp, *, linesep="\n", bufsize=4096):
    buf = ""
    pos = -1
    while True:
        if pos < 0:
            read = fp.read(bufsize)
            if not read:
                break

            buf += read
        else:
            yield buf[:pos + 1]
            buf = buf[pos + 1:]

        pos = buf.find(linesep)

    yield buf


# example usage

def example_usage():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-0", help="NUL separated lines", dest="sep", action="store_const",
        const="\x00", default="\n",
    )
    parser.add_argument("files", nargs="*")
    args = parser.parse_args()

    for line in fileinput_sep(args.files, linesep=args.sep):
        # do something with line
        print(line, end="")
