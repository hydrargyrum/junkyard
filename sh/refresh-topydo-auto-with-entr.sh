#!/bin/sh -eu

# - entr(1) takes a file list on stdin (here: ~/todo.txt) and tracks file
#   modifications
# - entr will re-run "topydo [...]" every time ~/todo.txt is modified,
#   this displays the most recent todo every time
# - "-s" is required because the given command ("topydo ...") has a pipe
#   and thus needs to be interpreted by a shell
# - "-cc" clears the terminal completely before running topydo
# - "-r" has the effect of hiding spurious message "xxx returned exit code 0"
#
# - "topydo | tac" displays most prioritary task at the bottom, because
#   it might scroll the terminal and we want the most prioritary to be shown
# - "-C256" keeps topydo colors even though it's piped ("| tac")

echo ~/todo.txt | entr -nscc "topydo -C256 | tac"
