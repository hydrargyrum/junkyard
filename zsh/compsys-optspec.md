# zshcompsys(1)'s `_arguments` syntax

| syntax    | accepts    | also accepts |
|:----------|:-----------|:-------------|
| `-foo:`   | `-foo ARG` |              |
| `-foo-:`  | `-fooARG`  |              |
| `-foo+:`  | `-fooARG`  | `-foo ARG`   |
| `-foo=:`  | `-foo=ARG` | `-foo ARG`   |
| `-foo=-:` | `-foo=ARG` |              |

The `-fooARG` makes more sense for single letter options: `-fARG`.
