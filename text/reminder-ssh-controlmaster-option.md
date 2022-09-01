# OpenSSH's [`ControlMaster`](https://manpages.debian.org/stable/ssh_config.5.en.html#ControlMaster) option

|         | try to use socket first | create socket | … only if not exists | verify ssh-askpass(1) |
|---------|-------------------------|---------------|----------------------|-----------------------|
|  `yes`  |                         |       ✔       |                      |                       |
|  `ask`  |                         |       ✔       |                      |           ✔           |
|  `no`   |            ✔            |               |                      |                       |
|  `auto` |            ✔            |       ✔       |          ✔           |                       |
|`autoask`|            ✔            |       ✔       |          ✔           |           ✔           |

- `yes` creates socket unconditionally and does not try to connect to it
- `no` will not create the socket but uses it if it exists
- `auto` is a mix of `no` and `yes`, it tries to connect to the socket and creates it else
- `ask` are variants that use `ssh-askpass(1)`
- socket path is set by `ControlPath` (a sensible value is `ControlPath ~/.ssh/sockets/%C.ssh`)