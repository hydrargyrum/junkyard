#!/usr/bin/env pytest
# SPDX-License-Identifier: WTFPL
# like `file.readlines()` but accepts an arbitrary delimiter

import io

import pytest


__all__ = ("iter_lines",)


def iter_lines(fp, delimiter=b"\n", *, bufsize=1024):
    """Reads lines from `fp` separated by `delimiter` and yield them"""
    if not isinstance(delimiter, (bytes, str)):
        raise TypeError(f"not a str or bytes: {delimiter!r}")

    buf = type(delimiter)()
    while True:
        chunk = fp.read(bufsize)
        if not chunk:
            if buf:
                yield buf
            break

        buf += chunk
        parts = buf.split(delimiter)
        buf = parts.pop(-1)
        for part in parts:
            yield part + delimiter


@pytest.mark.parametrize(
    "lines, delimiter",
    [
        (["foo\n", "bar\n", "baz"], b"\n"),
        (["foo\n", "bar\n", "baz\n"], b"\n"),
        (["foo\n", "bar" * 1024 + "\n", "baz\n"], b"\n"),
        (["foo\0", "bar" * 1024 + "\0", "baz"], b"\0"),
        (["fo\no\0", "b\nar" * 1024 + "\0", "baz\n"], b"\0"),
    ]
)
def test_iter_lines(lines, delimiter):
    lines = [line.encode() for line in lines]
    assert list(iter_lines(io.BytesIO(b"".join(lines)), delimiter)) == lines
