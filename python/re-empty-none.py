#!/usr/bin/env python3

# The "re" module can sometimes return matches with empty values or None.
# When? Let's discover by testing

import re

# We'll use a simple example: search for a number in a string

# 1. This is the basic case, the regex matches and finds something, so
# we get a `re.Match` object
assert re.search(r"(\d+)", "a123b").groups() == ("123",)

# 2. When nothing is found, our regex doesn't match, we have no `re.Match`
assert re.search(r"(\d+)", "ab") is None

# We'll use a more complex example: search for an assignment, optionnaly
# with a number (e.g. "a=42")

# 3. Allowing no digits in the regex, but digits in the string
assert re.search(r"(\w+)=(\d*)", "a=42b").groups() == ("a", "42")

# 4. Allowing no digits in the regex, without digits in the string
assert re.search(r"(\w+)=(\d*)", "a=b").groups() == ("a", "")

# 5. But we can also make the digit group optional
assert re.search(r"(\w+)=(\d+)?", "a=b").groups() == ("a", None)

# the end.
if __name__ == "__main__":
    print("read the source code instead")
