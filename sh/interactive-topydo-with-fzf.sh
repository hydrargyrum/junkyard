#!/bin/sh -eu
# SPDX-License-Identifier: WTFPL

# [topydo](https://github.com/topydo/topydo) is a CLI todo-list manager

# here's how to use [fzf](https://github.com/junegunn/fzf) to make an
# interactive UI around topydo

# honor [NO_COLOR](https://no-color.org/) and related env vars
has_color=
if [ -n "${NO_COLOR:+anything}" ]
then
	has_color=
elif [ -n "${FORCE_COLOR:+anything}" ]
then
	has_color=y
elif [ -n "${CLICOLOR_FORCE:+anything}" ]
then
	has_color=y
elif [ -t 1 ] # is stdout a tty?
then
	has_color=y
fi

# FZF_DEFAULT_COMMAND is read by fzf and run on start (as we don't feed stdin)
cmd="topydo -a -t $1"
export FZF_DEFAULT_COMMAND="$cmd ${has_color:+-C256}"
# but if we want to get fresh todo, we need to tell it manually to run
# $FZF_DEFAULT_COMMAND again. Warning: this var is not read by fzf itself,
# we'll use it later
reload="reload($FZF_DEFAULT_COMMAND)"

# add a custom help screen
help=$(cat <<- EOF
	ctrl-t: mark selected entry as done
	ctrl-e: edit selected entry
	ctrl-n: add an entry using the search query text as description
	ctrl-d: delete selected entry
	ctrl-r: to reload display (and quit this help screen)
	f1: show this help screen
	ctrl-q: quit app
EOF
)

# `--bind "SHORTCUT:FUNCTIONS"`
# `+` to run several fzf functions
# we use `+reload(...)` often as every topydo action will affect the todo list
# topydo stdout has format `|id| text`, so we use `{2}` to extract the id
fzf \
	${has_color:+--ansi} \
	--delimiter='\|' \
	--bind "ctrl-r:$reload" \
	--bind "ctrl-e:execute($cmd edit {2})+$reload" \
	--bind "ctrl-t:execute($cmd do {2})+$reload" \
	--bind "ctrl-n:execute($cmd add {q})+$reload" \
	--bind "ctrl-d:execute($cmd del {2})+$reload" \
	--bind "f1:reload(printf '$help')"

# ctrl-n: we need to input a new entry, but fzf is merely a filterer…
# let's use `{q}` (the search field) to build a new entry!
