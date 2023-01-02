# What exit code will grep use?

`grep` exits with different codes if it found matches or not.

## The rules are

- **for normal search, `grep` returns 0 if at least one line matches the pattern, and 1 if no line matches**
- **for exclusive search (`grep -v`), `grep` returns 0 if at least one line did not match the pattern, and 1 if all lines matched**

Another way to see it: if you don't pass `-q`, does it print any lines?

- if it prints anything, grep returns 0
- if it prints nothing, grep returns 1

## Test it yourself

Input files:

- `echo foo > foo.txt`
- `echo bar > bar.txt`
- `{ echo foo ; echo echo bar ; } > foo-bar.txt`
- `true > empty.txt`

| file        | grep foo | grep bar | grep baz | grep -v foo | grep -v bar | grep -v baz |
|:------------|:---------|:---------|:---------|:------------|:------------|:------------|
| foo.txt     | 0        | 1        | 1        | 1           | 0           | 0           |
| bar.txt     | 1        | 0        | 1        | 0           | 1           | 0           |
| foo-bar.txt | 0        | 0        | 1        | 0           | 0           | 0           |
| empty.txt   | 1        | 1        | 1        | 1           | 1           | 1           |
