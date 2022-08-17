#!/usr/bin/env python3

import prettytable

tab = prettytable.PrettyTable(["foo", "bar"])
tab.add_row([1, 2])
tab.add_row([3, 4])

tab.hrules = prettytable.HEADER
tab.junction_char = "|"

print(tab)
