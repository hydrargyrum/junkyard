# lazily generate entry values of an enum basing on entry names

from enum import Enum, auto


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    FOO = auto()
    BAR = auto()


class AutoNameLower(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

    FOO = auto()
    BAR = auto()
    # avoids typos like: SOMETHING = "smoething"


assert AutoName.FOO.name == "FOO"
assert AutoName.FOO.value == "FOO"

assert AutoNameLower.FOO.name == "FOO"
assert AutoNameLower.FOO.value == "foo"
