#!/bin/sh -eu

# Copy to selection (paste with middle-click)
xclip -i < copied.txt
xsel -i < copied.txt

# Copy to clipboard
xclip -i -selection CLIPBOARD < copied.txt
xsel -i -b < copied.txt

# Get selection (middle-click)
xclip -o > pasted.txt
xsel -o > pasted.txt

# Get clipboard
xclip -o -selection CLIPBOARD > pasted.txt
xsel -o -b > pasted.txt
