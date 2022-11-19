#!/bin/sh -eu

# This script assumes your /etc/hosts contains a zone delimited with
# a "# auto docker start" comment and a "# auto docker stop" comment
# That zone will be modified automatically by this script and manual
# modifications made in it will be overwritten by this script.

target=/etc/hosts
tmpf=$(mktemp -t hosts.XXXXXX)

# assert the delimiters are present
if ! grep -q "# auto docker start" "$target"
then
	echo 'Missing "# auto docker start" delimiter' >&2
	exit 1
fi
if ! grep -q "# auto docker stop" "$target"
then
	echo 'Missing "# auto docker stop" delimiter' >&2
	exit 1
fi

# prologue: verbatim copy everything before start delimiter
sed '/# auto docker start$/ q' "$target" > "$tmpf"

# generate hosts entries
docker ps --format '{{.Names}}' | while read name
do
	addr=$(docker inspect -f '{{.NetworkSettings.Networks.shared_net.IPAddress}}' "$name" | grep -v value) || continue
	echo "$addr $name"
done >> "$tmpf"

# epilogue: verbatim copy everything after end delimiter
sed -n '/# auto docker stop/,$ p' "$target" >> "$tmpf"

# replace /etc/hosts if `-f` was given
if [ "${1-}" = -f ]
then
	cat "$tmpf" > "$target"
else
	cat "$tmpf"
fi
