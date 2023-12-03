#!/bin/false

# sponge allows you to fix the broken:
some-command < some-file.txt > some-file.txt

# with:
some-command < some-file.txt | sponge some-file.txt

# examples

# sort and uniq lines in-place:
sort -u < some-file.txt | sponge some-file.txt

# expand tabs to 4 spaces in-place:
expand -t4 somefile.py | sponge somefile.py

# indent a json file in-place:
python3 -m json.tool somefile.json | sponge somefile.json

# sed on TTY, display results only when the input is finished
# so input and output are distinguishable in terminal display:
sed 's/some/thing/g' somepattern | sponge

# WARNING: if the "producer" command fails, sponge still overwrites the file
awk '{ print $2 ' some-file.txt | sponge some-file.txt
# oops syntax error in awk expression: awk quits without printing anything
# oops sponge wrote an empty some-file.txt, destroying the file!
