#!/bin/sh -eu

# __MACOSX folders are annoying folders created by macOS, remove them

# - use -0/-z flags on the whole pipeline not to break when a space or newline is present in a folder name
# - grep 'OSX$' to prevent locate from finding the folders' contents
# - rm -r to remove folders, -v for verbosity

locate -0 __MACOSX | grep -z 'OSX$' | xargs -0 rm -r -v
