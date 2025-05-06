# List key bindings in various apps

## bash

Within bash, type `bind -v`

For the default bindings, run `INPUTRC=/dev/null bash -c 'bind -v'`

## mpv

When mpv is running, press `shift+i` and then `4`. Can scroll with `up arrow`/`down arrow`. Press `4` again to hide.

See also `mpv --input-keylist` and `mpv --input-cmdlist`

## tig

When tig is running, press `h` or type `:view-help`

Or run `TIG_SCRIPT=<(echo :view-help) tig`

## visidata

Press `z` then `ctrl+h` to open a sheet with commands and their bindings.

## zsh

Within zsh, type `bindkey` or `bindkey -M keymap_name`. Can view list of keymaps with `bindkey -l`

Run within `zsh -f` to skip loading dotfiles.
