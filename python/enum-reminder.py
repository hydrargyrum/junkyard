#!/usr/bin/env python3

import enum


class E(enum.Enum):
    UPPER = "lower"


print("### repr vs str")

print("repr(E.UPPER): ", end="")
print(repr(E.UPPER))
# prints: <E.UPPER: 'lower'>

print("str(E.UPPER): ", end="")
print(str(E.UPPER))
# prints: E.UPPER

print("### enum entry fields")

print("repr(E.UPPER.name): ", end="")
print(repr(E.UPPER.name))
# prints: 'UPPER'

print("repr(E.UPPER.value): ", end="")
print(repr(E.UPPER.value))
# prints: 'lower'

print("### promote value to enum")

print('repr(E("lower")): ', end="")
print(repr(E("lower")))
# prints: <E.UPPER: 'lower'>

print('repr(E["UPPER"]): ', end="")
print(repr(E["UPPER"]))
# prints: <E.UPPER: 'lower'>

print("### listing entries")

print("list(E): ", end="")
print(list(E))
# prints: [<E.UPPER: 'lower'>]
