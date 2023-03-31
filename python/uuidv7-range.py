
"""
UUIDv7 format:

    UUUUUUUUUSSS-VSSS-MRRR-RRRRRRRRRRRR

where:

- U is unix timestamp in seconds since epoch (36 bits, 9 hex digits)
- S is sub-second value of unix timestamp (24 bits, 6 hex digits)
- V is UUID "version" and is always 7 (4 bits, 1 hex digit)
- M is 4 bits which are a mix of:
  - 2 bits for UUID "variant", always 0b10
  - 2 bits of R, see below
- R is random bits (62 bits, 2 are in the M part)

"""


def _convert_ts(ts):
    s = "%09x" % ts
    return f"{s[:8]}-{s[8]}"


# set all subsecond bits to 0, all random bits to 0, but keep V and M untouched
START_PREFIX = "000-7000-8000-000000000000"

# set all subsecond bits to 0, all random bits to 1, but keep V and M untouched
END_PREFIX = "fff-7fff-Bfff-ffffffffffff"


def uuidv7_range(ts1, ts2):
    ts1 = int(ts1)
    ts2 = int(ts2)
    return (
        _convert_ts(ts1) + START_PREFIX,
        _convert_ts(ts2) + END_PREFIX,
    )
