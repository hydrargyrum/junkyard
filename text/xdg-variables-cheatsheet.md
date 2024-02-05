# `XDG_*` variables cheatsheet

| Environment variable | Default value | Scope | Contents | Description |
|---|---|---|---|---|
| `$XDG_CONFIG_DIRS` | `/etc/xdg` | system | configuration files | |
| `$XDG_CONFIG_HOME` | `$HOME/.config` | user | configuration files | |
|||||
| `$XDG_DATA_DIRS` | `/usr/local/share/:/usr/share/` | system | data files | |
| `$XDG_DATA_HOME` | `$HOME/.local/share` | user | data files | |
|||||
| `$XDG_STATE_HOME` | `$HOME/.local/state` | user | state files | state data that should persist between (application) restarts, but that is not important or portable enough to the user that it should be stored in `$XDG_DATA_HOME`. Examples: actions history (logs, history, recently used files, …), current state of the application that can be reused on a restart (view, layout, open files, undo history, …) |
| `$XDG_CACHE_HOME` | `$HOME/.cache` | user | non-essential data files | |
| `$XDG_RUNTIME_DIR` | no default | user | non-essential runtime files | runtime files and other file objects (such as sockets, named pipes, ...). No large files, it might reside in runtime memory. This folder is created by the system, and files in the directory will not survive reboot or a full logout/login cycle. |

Based on [XDG Base Directory Specification 0.8](https://specifications.freedesktop.org/basedir-spec/0.8/)

See also [Archlinux notes](https://wiki.archlinux.org/title/XDG_Base_Directory#User_directories)
