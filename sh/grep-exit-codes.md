# What exit code will grep use?

`grep` exits with different codes if it found matches or not.

## The rules are

- for normal search, `grep` returns **0 if at least one line DID match the pattern**, and 1 if no line matches
- for exclusive search (`grep -v`), `grep` returns **0 if at least one line DID NOT match the pattern**, and 1 if no line did not match

Another way to see it: does `grep` print any lines (without `-q`)?

- if it prints anything, grep returns 0
- if it prints nothing, grep returns 1

Corollary: when `grep` receives an empty file, with or without `-v`, it always returns 1.

## Test it yourself

Input files:

```sh
echo foo > foo.txt
echo bar > bar.txt
cat foo.txt bar.txt > foo-bar.txt
true > empty.txt
```

| command     | foo.txt | bar.txt | foo-bar.txt | empty.txt |
| :-----------| :-------| :-------| :-----------| :---------|
| grep foo    | 0       | 1       | 0           | 1         |
| grep bar    | 1       | 0       | 0           | 1         |
| grep baz    | 1       | 1       | 1           | 1         |
| grep -v foo | 1       | 0       | 0           | 1         |
| grep -v bar | 0       | 1       | 0           | 1         |
| grep -v baz | 0       | 0       | 0           | 1         |
