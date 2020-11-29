# usage: . ./zsh-options-status.zsh
#
# Show zsh options (see man page zshoptions(1)) and their status
# starting with a "+" if it's enabled, or with "-" if it's disabled.
#
# Why? zsh has `setopt` and `unsetopt` commands to display options,
# but that's 2 commands, and `setopt` shows some disabled options
# and `unsetopt` shows some enabled options.
# `zsh-options-status.zsh` combines the display in a single command
# with explicit enabled/disabled status.

zsh-options-status () {
	local name

	{
		setopt | while { read name } {
			name=+${name/#no/-}
			name=${name/#+-/-}
			echo "$name"
		}
		unsetopt | while { read name } {
			name=-${name/#no/+}
			name=${name/#-+/+}
			echo "$name"
		}
	} | sort
}

zsh-options-status
