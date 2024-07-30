# fzf `{placeholders}`

## What are fzf placeholders?

[`fzf`](https://github.com/junegunn/fzf) supports `{placeholders}` in various parts, for example with `--preview` or with `--bind`.
For example: `fzf --preview 'cat {}'` will preview current selected file by displaying its content with `cat(1)`.
Here, `{}` will be replaced by the text of current entry, which will be passed to `cat` as a single argument (even if it contains spaces).

## Syntax

Placeholders can do finer manipulation than just "current text".

In the following table, suppose `fzf --multi` receives 2 lines as input:

```
foo bar
baz qux
```

and both lines are selected with `<tab>`.

| Placeholder | Values                  | Description                                   |
|-------------|-------------------------|-----------------------------------------------|
| `{}`        | `baz qux`               | Last selected line                            |
| `{+}`       | `foo bar` and `baz qux` | all selected lines as separate args           |
| `{1}`       | `baz`                   | First word of last selected line              |
| `{2}`       | `qux`                   | Second word of last selected line             |
| `{+1}`      | `foo` and `baz`         | First word of all selected lines              |
| `{+2}`      | `bar` and `qux`         | Second word of all selected lines             |
| `{n}`       | `1`                     | Last selected line number (starting with 0)   |
| `{+n}`      | `0` and `1`             | Selected lines numbers (starting with 0)      |
| `{+f}`      | `/tmp/fzf-preview-xxx`  | Temp file path containing only selected lines |

As a general rule, `+` works as a prefix with multiple selected items.


## How to reproduce?

`printf "foo bar\nbaz qux\n" | fzf --multi --bind 'enter:become(show-args {})'`

Then select all lines and press enter.
