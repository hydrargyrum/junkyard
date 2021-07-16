#!/usr/bin/env python3

import prettytable

tab = prettytable.PrettyTable(["foo", "bar"])
tab.add_row([1, 2])
tab.add_row([3, 4])

print(tab)
print()

tab.vertical_char, tab.horizontal_char, tab.junction_char = "│─┼"
print(tab)
print()

tab.vertical_char, tab.horizontal_char, tab.junction_char = "║═╬"
print(tab)
print()

tab.vertical_char, tab.horizontal_char, tab.junction_char = "┃━╋"
print(tab)
print()
