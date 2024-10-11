#!/bin/sh -eu
# parses [rdfind](https://rdfind.pauldreik.se/)'s results.txt and
# - colors and indents lines
# - prints human-readable size
# - adds hyperlinks

# {{{ helper functions
color () {
	# use standard terminfo, not non-standard hardcoded escape sequences
	case $1 in
		red)
			coloring=1 ;;
		green)
			coloring=2 ;;
		*)
			return
	esac
	# no need to hardcode a terminal sequence: tput will use the right sequence
	# that current terminal supports
	tput setaf "$coloring"
}

resetcolor () {
	tput sgr0
}

hyperlink () {
	# unfortunately, there is no terminfo entry for this
	printf '\033]8;;%s\033\134%s\033]8;;\033\134' "file://$(echo "$1" | urlencode)" "$2"
}

urlencode () {
	# modified version of https://gist.github.com/moyashi/4063894
	awk '
		BEGIN {
			for (i = 0; i <= 255; i++) {
			ord[sprintf("%c", i)] = i
		}
	}
	function escape(str, c, len, res) {
		len = length(str)
		res = ""
		for (i = 1; i <= len; i++) {
			c = substr(str, i, 1);
			if (c ~ /[0-9A-Za-z\/.]/)
				res = res c
			else
				res = res "%" sprintf("%02X", ord[c])
		}
		return res
	}
	{ print escape($0) }
	'
}

humansize () {
	sz=$1
	# el-cheapo array since POSIX sh doesn't have arrays
	set -- "" K M G T

	# - we can only divide if there's a "next" value in array, so check there
	# are 2 or more elements.
	# - since there's no float division in shell, check >= 10 and do a last
	# division later
	while [ $# -ge 2 ] && [ $((sz / 1000)) -ge 10 ]
	do
		shift
		sz=$((sz / 1000))
	done
	if [ $# -ge 2 ] && [ "$sz" -gt 1000 ]
	then
		# here, 1000 < sz <= 9999, and there's a unit left
		# do our custom division so we have the first decimal digit
		shift
		sz=$(floatdiv "$sz" 1000)
	fi
	echo "$sz ${1}b"
}

floatdiv () {
	# POSIX shell cannot do division with decimals, let's do it by ourselves
	# (with truncation, not rounding)
	echo "$(( $1 / $2 )).$(( ($1 * 10 / $2) % 10 ))"
}

absolutepath () {
	( cd "$1" && pwd )
}
# }}}

usage () {
	cat <<- EOF
		usage: $0 PATH

		View a rdfind results.txt file located at PATH.
		https://rdfind.pauldreik.se/
	EOF
}

# main loop
dir=$PWD
case $# in
	0) ;;
	1)
		if [ "$1" = -h ] || [ "$1" = --help ]
		then
			usage
			exit 0
		fi
		dir=$(absolutepath "$(dirname "$1")")
		# read file to stdin
		exec < "$1"
		;;
	*)
		usage >&2
		exit 64  # EX_USAGE
		;;
esac

while read duptype id depth size device inode priority name
do
	target=$name
	if [ "$name" = "${name#/}" ]
	then
		target="$dir/$name"
	fi

	case "$duptype" in
		"#")
			continue
			;;

		DUPTYPE_FIRST_OCCURRENCE)
			echo "$(color green)$duptype $(humansize $size)" \
				"$(hyperlink "$target" "$name")$(resetcolor)"
			;;

		DUPTYPE_OUTSIDE_TREE|DUPTYPE_WITHIN_SAME_TREE)
			echo "    $(color red)$duptype $(humansize $size)" \
				"$(hyperlink "$target" "$name")$(resetcolor)"
			;;
	esac
done
