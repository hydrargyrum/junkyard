# Collection of personal random snippets and cheatsheets

## Non-tech
- [`reminder-am-pm-times.rst`](text/reminder-am-pm-times.rst): a cheatsheet for the unintuitive AM/PM times
- [`street-numbers/`](text/street-numbers/): find in what direction street number increase by looking at a single number

## Text
- [`borgbackup-samples.md`](text/borgbackup-samples.md): examples of how to use [borgbackup](https://www.borgbackup.org/)
- [`commands-with-sub-manual-pages.yml`](commands-with-sub-manual-pages.yml): commands which have dedicated sub manual pages for subcommands
- [`howto-do-shellextension-with-qt`](text/howto-do-shellextension-with-qt): an old tutorial on how to implement windows shell extension in qt, for example to overlay icons in `explorer.exe`
- [`reminder-ssh-controlmaster-option.md`](text/reminder-ssh-controlmaster-option.md): reminder for ssh's [ControlMaster](https://manpages.debian.org/stable/openssh-client/ssh_config.5.en.html#ControlMaster)
- [`xdg-variables-cheatsheet.md`](text/xdg-variables-cheatsheet.md): [`XDG_*`](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html) variables cheatsheet
- [`xscreensaver-theme-colors/`](text/xscreensaver-theme-colors/): cheatsheet of theme configuration resources for [xscreensaver](https://www.jwz.org/xscreensaver/)

## C++
- [`asciitree.cpp`](cpp/asciitree.cpp): C++ example to hardcode tree structures that look like trees in source
- [`diy-QReadWriteLock.cpp`](cpp/diy-QReadWriteLock.cpp): for qt, DIY implementation of qreadwritelock
- [`diy-strong-ptr-and-weak-ptr.cpp`](cpp/diy-strong-ptr-and-weak-ptr.cpp): DIY implementation of strong and weak pointers

## Config
- [`todotxt.nanorc`](dotfiles/todotxt.nanorc): [`nano`](https://www.nano-editor.org/) syntax coloring for [`todo.txt` format](http://todotxt.org/)

## gitlab-ci
- [`cache-for-debian-based-images.gitlab-ci.yml`](gitlab/cache-for-debian-based-images.gitlab-ci.yml): snippet for caching Debian packages to avoid re-downloading them
- [`cache-for-python.gitlab-ci.yml`](gitlab/cache-for-python.gitlab-ci.yml): snippet for caching pip packages to avoid re-downloading them

## Javascript
- [`break-url-bar.html`](javascript/break-url-bar.html): somehow break URL bar display
- [`greasemonkey/deliveroo`](javascript/greasemonkey/deliveroo): in [greasemonkey/violentmonkey](https://addons.mozilla.org/firefox/addon/violentmonkey/) js, various scripts to make deliveroo site a bit less painful
- [`greasemonkey/round-prices.user.js`](javascript/greasemonkey/round-prices.user.js): in [greasemonkey/violentmonkey](https://addons.mozilla.org/firefox/addon/violentmonkey/) js, round numeric values on any web page, for example replace "9.99€" to "~10€"
- [`greasemonkey/reddit-ignoreusers.user.js`](javascript/greasemonkey/reddit-ignoreusers.user.js): in [greasemonkey/violentmonkey](https://addons.mozilla.org/firefox/addon/violentmonkey/) js, hide topics created by some (configurable) users

## Python
- [`always_sorted_list.py`](python/sorted_list.py): a list data structure whose values are always sorted (if the values are immutable)
- [`ansi_box.py`](python/ansi_box.py): toy library for drawing stuff with ansi sequences
- [`autoimport-pyqt5.toml`](python/autoimport-pyqt5.toml): [autoimport](https://lyz-code.github.io/autoimport/) config for PyQt5 imports and its [generator script](python/autoimport-pyqt5-config-generator.py)
- [`better_sum.py`](python/better_sum.py): improving on python's `sum` builtin to accept non number types, like lists or timedeltas
- [`cheap_sqlite_schema_migration.py`](python/cheap_sqlite_schema_migration.py): for python [sqlite](https://docs.python.org/3/library/sqlite3.html), cheap snippet of how to performed versioned database migrations (schema or not)
- [`collections-abc-classes.md`](python/collections-abc-classes.md): [Mermaid](https://mermaid.js.org/) diagram showing `collections.abc` classes with abstract methods and mixins
- [`enum-reminder.py`](python/enum-reminder.py): reminder on [enums](https://docs.python.org/3/library/enum.html)
- [`python/file_mode_to_string_like_ls.py`](python/file_mode_to_string_like_ls.py): convert a `stat()` file mode to a string like `-rwxr-xr-x`
- [`gfs-backup-rotation-algorithm.py`](python/gfs-backup-rotation-algorithm.py): [GFS (Grandfather-father-son)](https://en.wikipedia.org/wiki/Backup_rotation_scheme#Grandfather-father-son) backup rotation scheme
- [`gitlab-delete-your-comments.py`](python/gitlab-delete-your-comments.py): delete all of your MR comments on a Gitlab instance
- [`graphql-queries.py`](python/graphql-queries.py): perform GraphQL queries/mutations
- [`human_sorted_filenames.py`](python/sorted_filenames.py): sort filenames "for humans", not merely with ASCII order
- [`intervals.py`](python/intervals.py): data structure to hold intervals
- [`merge-docker-compose-files.py`](python/merge-docker-compose-files.py): merge several docker-compose.yml files together
- [`merge_iterables.py`](python/merge_iterables.py): python function to merge several sorted iterables into a single big sorted iterable, on the fly
- [`os_walk_no_xdev.py`](python/os_walk_no_xdev.py): wraps `os.walk()` but doesn't enter mountpoints/other filesystems
- [`pyproject-snippets.md`](python/pyproject-snippets.md): `pyproject.toml` snippets
- [`pytest-kludgy-parametric-fixtures`](python/pytest-kludgy-parametric-fixtures): for python's [pytest](https://docs.pytest.org/), snippet of an alternate way to do parametric fixtures, within different directories
- [`re-empty-none.py`](python/re-empty-none.py): the [`re`](https://docs.python.org/3/library/re.html) module can sometimes return matches with empty values or None
- [`requests-get-server-ip-in-response.py`](python/requests-get-server-ip-in-response.py): for [requests](https://pypi.org/project/requests/) lib, how to get the server ip address in the Response object
- [`unpack-dict-params-to-pydantic.py`](python/unpack-dict-params-to-pydantic.py): for [pydantic](https://pypi.org/project/pydantic/) lib, decorator to convert json arguments to objects automatically
- [`uuidv7-range.py`](python/uuidv7-range.py): range of [UUIDv7](https://www.ietf.org/archive/id/draft-peabody-dispatch-new-uuid-format-04.html#name-uuid-version-7) values between 2 timestamps, for example for partitioning

## `sh`
- [`add-containers-in-hosts-file.sh`](sh/add-containers-in-hosts-file.sh): add docker container addresses in `/etc/hosts`, with the container names
- [`date-in-email-header-format-rfc2822.sh`](sh/date-in-email-header-format-rfc2822.sh): print date in rfc2822 format (suitable for email headers), also useful for any strftime implementation
- [`example-chezmoi-conf-in-docker.sh`](sh/example-chezmoi-conf-in-docker.sh): how to export your [chezmoi](https://www.chezmoi.io/) dotfiles and import them easily in a docker container
- [`examples-of-how-cool-is-sponge.sh`](sh/examples-of-how-cool-is-sponge.sh): examples of how cool is sponge(1)
- [`find-permissions.sh`](sh/find-permissions.sh): small GNU [`find(1)`](https://manpages.debian.org/stable/find) snippets for dealing with permissions
- [`grep-exit-codes.md`](sh/grep-exit-codes.md): what exit code will grep use?
- [`guru-meditation.sh`](sh/guru-meditation.sh): generate colored ANSI ["guru meditation"](https://en.wikipedia.org/wiki/Guru_Meditation) banner using POSIX sh and `tput`
- [`interactive-topydo-with-fzf.sh`](sh/interactive-topydo-with-fzf.sh): create an interactive UI for [topydo](https://github.com/topydo/topydo) with [fzf](https://github.com/junegunn/fzf)
- [`rdfind-resultstxt-coloring.sh`](sh/rdfind-resultstxt-coloring.sh): view [rdfind](https://rdfind.pauldreik.se/)'s results.txt, demonstrating coloring without hardcoded sequences, hyperlinks
- [`refresh-topydo-auto-with-entr.sh`](sh/refresh-topydo-auto-with-entr.sh): refresh automatically [topydo](https://github.com/topydo/topydo) (todo.txt) display using entr
- [`remove-all-osx-cache-dirs.sh`](sh/remove-all-osx-cache-dirs.sh): remove all `__MACOSX` cache dirs with locate and xargs
- [`sysexits-values.sh`](sh/sysexits-values.sh): standard `exit(1)` code constants
- [`ttrss-to-shaarli.sh`](sh/ttrss-to-shaarli.sh): script to export ttrss starred articles and import them in [Shaarli](https://github.com/shaarli/Shaarli)
- [`xclip-or-xsel.sh`](sh/xclip-or-xsel.sh): mini-cheatsheet to [`xclip`](https://github.com/astrand/xclip) and [`xsel`](https://github.com/kfish/xsel) (manipulate X11 clipboard from command-line)

## `zsh`
- [`find-termcap-name.zsh`](zsh/find-termcap-name.zsh): take a key as input, then print the corresponding termcap name
- [`options-status.zsh`](zsh/options-status.zsh): show current status of all options (think setopt/unsetopt)
- [`print-all-termcaps.zsh`](zsh/print-all-termcaps.zsh): print all termcap names and values (in hex, with `xxd(1)`, for readability)
- [`print-associative.zsh`](zsh/print-associative.zsh): print keys and values of an associative array zsh variable
- [`remove-empty-files-with-glob-quals.zsh`](zsh/remove-empty-files-with-glob-quals.zsh): using glob quals (metadata matching), remove empty files
- [`zmv-rename-files-keeping-their-extension.zsh`](zsh/zmv-rename-files-keeping-their-extension.zsh): using [zmv](https://grml.org/zsh/zsh-lovers.html#_zmv_examples_require_autoload_zmv), rename files and keeping their extension


All content here is licensed under the UNLICENSE. See UNLICENSE file.
