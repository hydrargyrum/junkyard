#!/bin/false

# remove empty files:
# - name matches "*" (any name)
# - entry is a file: "."
# - size (Length) is 0: "L0"
rm -v *(.L0)

# "*" is the glob pattern (for file names)
# "(.L0)" are the glob qualifiers (for metadata)

# and recursively:
rm -v **(.L0)

# as an alternative to:
find -maxdepth 1 -size 0 -exec rm -v "{}" +  # not recursive
find -size 0 -exec rm -v "{}" +  # recursively
