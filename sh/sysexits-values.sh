#!/bin/false

# These are standard exit codes. This snippet can be included in a shell file.
# Sample:
#
#   if [ $# -lt 1 ]; then
#       echo "usage: $0 ARGS" >&2
#       exit $EX_USAGE
#   fi
#   # do something valuable
#   exit $EX_OK
#
# Feel free to only include part of the snippet, defining only the values you
# actually use, or even to hardcode the value (though it may be less explicit
# for the next person reading your script).
#
# These codes come from https://man.openbsd.org/sysexits but are used on non-BSD systems too!

EX_OK=0
# Successful exit

EX_USAGE=64
# The command was used incorrectly, e.g., with the wrong number of arguments, a bad flag, bad syntax in a parameter, or whatever.

EX_DATAERR=65
# The input data was incorrect in some way. This should only be used for user's data and not system files.

EX_NOINPUT=66
# An input file (not a system file) did not exist or was not readable. This could also include errors like “No message” to a mailer (if it cared to catch it).

EX_NOUSER=67
# The user specified did not exist. This might be used for mail addresses or remote logins.

EX_NOHOST=68
# The host specified did not exist. This is used in mail addresses or network requests.

EX_UNAVAILABLE=69
# A service is unavailable. This can occur if a support program or file does not exist. This can also be used as a catch-all message when something you wanted to do doesn't work, but you don't know why.

EX_SOFTWARE=70
# An internal software error has been detected. This should be limited to non-operating system related errors if possible.

EX_OSERR=71
# An operating system error has been detected. This is intended to be used for such things as “cannot fork”, or “cannot create pipe”. It includes things like getuid(2) returning a user that does not exist in the passwd file.

EX_OSFILE=72
# Some system file (e.g., /etc/passwd, /var/run/utmp) does not exist, cannot be opened, or has some sort of error (e.g., syntax error).

EX_CANTCREAT=73
# A (user specified) output file cannot be created.

EX_IOERR=74
# An error occurred while doing I/O on some file.

EX_TEMPFAIL=75
# Temporary failure, indicating something that is not really an error. For example that a mailer could not create a connection, and the request should be reattempted later.

EX_PROTOCOL=76
# The remote system returned something that was “not possible” during a protocol exchange.

EX_NOPERM=77
# You did not have sufficient permission to perform the operation. This is not intended for file system problems, which should use EX_NOINPUT or EX_CANTCREAT, but rather for higher level permissions.

EX_CONFIG=78
# Something was found in an unconfigured or misconfigured state.
