#!/usr/bin/env pytest

from datetime import timedelta
from functools import reduce
import operator

import pytest


# sum() is a pretty dumb function
def test_sum_is_dumb():
    with pytest.raises(TypeError):
        sum(["a", "b", "c"])
    with pytest.raises(TypeError):
        sum([timedelta(1), timedelta(2), timedelta(3)])


# same as sum(), but smarter for types
# but, it only accounts for typing and doesn't allow parallelization
def better_sum(iterable, /):
    return reduce(operator.add, iterable)


def test_better_sum():
    assert sum([1, 2, 3]) == 6
    assert better_sum(["a", "b", "c"]) == "abc"
    assert better_sum([timedelta(1), timedelta(2), timedelta(3)]) == timedelta(6)
