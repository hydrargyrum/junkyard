#!/bin/sh -eu
# shellcheck enable=

# "set -o pipefail" does not exist in posix shell
# but we can emulate it with pure POSIX and some snake oil

# prologue: helper functions and vars

pids=
pipe1=
pipe2=
counter=0
# we'll be generating many pipes, cleanup will be easier if they all are
# in a dedicated directory
pipedir=$(mktemp -d -t pipes.XXXXXX)

trap 'rm -f "$pipedir"/*.fifo && rmdir "$pipedir"' EXIT

# left side of a pipe: "foo |"
left () {
	pipe1="$pipedir/$counter.fifo"
	counter=$(( counter + 1 ))
	mkfifo "$pipe1"
	"$@" > "$pipe1" &
	pids="$pids $!"
}

# right side of a pipe: "| foo"
right () {
	"$@" < "$pipe1" &
	pids="$pids $!"
}

# middle side of a pipe: "| foo |"
middle () {
	pipe2="$pipedir/$counter.fifo"
	counter=$(( counter + 1 ))
	mkfifo "$pipe2"
	"$@" < "$pipe1" > "$pipe2" &
	pids="$pids $!"
	pipe1="$pipe2"
}

wait_pipes () {
	for pid in $pids
	do
		wait "$pid"
		# "wait" returns the exit code of $pid
		# i.e. if there's "set -e", wait will exit the shell if the waited
		# command exited with an error (that's the trick to emulate
		# pipefail)
	done
	pids=
}

# this is how to use it

# instead of "ls / | grep etc", we do
left ls /
right grep etc
wait_pipes

# instead of "ls / | sed s/c/C/ | sed s/e/E/ | grep etc", we do
left ls /
middle sed s/c/C/
middle sed s/e/E/
right grep EtC
wait_pipes

# in order to run "false | true", we do
left false
right true
wait_pipes
