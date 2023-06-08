#!/usr/bin/env python3

import enum


class E(enum.Enum):
    UPPER = "lower"


print(repr(E.UPPER))
# <E.UPPER: 'lower'>

print(str(E.UPPER))
# E.UPPER

print(repr(E("lower")))
# <E.UPPER: 'lower'>

print(repr(E.members["UPPER"]))
# <E.UPPER: 'lower'>

E.UPPER.name == 'UPPER'

E.UPPER.value == 'lower'
