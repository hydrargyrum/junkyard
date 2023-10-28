#!/bin/sh -eu
# 2012-09-04

COLUMNS=$(tput cols)

spaces () {
	head -c "$1" < /dev/zero | tr '\000' ' '
}

red () {
	tput setab 1
	spaces $1
	tput sgr0
}

red $COLUMNS
echo

red 1
spaces $((COLUMNS - 2))
red 1
echo

for line
do
	lenarg=$(printf %s "$line" | wc -m)
	red 1
	pos=$(( ( COLUMNS - 1 - lenarg ) / 2 ))
	#pos=30
	spaces $((pos - 1))
	tput setaf 1
	printf %s "$line"
	tput sgr0
	spaces $(( COLUMNS - pos - 1 - lenarg ))
	red 1
	echo

	red 1
	spaces $((COLUMNS - 2))
	red 1
	echo
done

red $COLUMNS
echo
