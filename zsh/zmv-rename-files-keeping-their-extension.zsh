#!/bin/false

# rename in one command:
# - foo.md -> bar.md
# - foo.html -> bar.html
# - foo.pdf -> bar.pdf
# but not:
# - qux.html

zmv -v 'foo.(*)' 'bar.$1'

# and do the same with git mv

zmv -p "git mv" -v 'foo.(*)' 'bar.$1'
