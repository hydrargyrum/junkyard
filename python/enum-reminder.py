#!/usr/bin/env python3

import enum


class E(enum.Enum):
    UPPER = "lower"


### repr vs str

print(repr(E.UPPER))
# prints: <E.UPPER: 'lower'>

print(str(E.UPPER))
# prints: E.UPPER

### promote value to enum

print(repr(E("lower")))
# prints: <E.UPPER: 'lower'>

print(repr(E["UPPER"]))
# prints: <E.UPPER: 'lower'>

### enum entry fields

assert E.UPPER.name == 'UPPER'

assert E.UPPER.value == 'lower'
