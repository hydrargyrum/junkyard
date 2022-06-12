#!/bin/sh -eu

# outputs current date and time in email `Date` header format
# this follows RFC 2822

export LANG=C
date +"%a, %d %b %Y %H:%M:%S %z"
