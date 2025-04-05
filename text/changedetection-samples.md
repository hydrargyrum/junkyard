# [ChangeDetection](https://github.com/dgtlmoon/changedetection.io) samples

## Following any github project's releases

For example, to follow releases of <https://github.com/caddyserver/caddy>

- Use this URL: `https://api.github.com/repos/caddyserver/caddy/releases?per_page=1`
- Use JSONPath filter ("filters and triggers" tab): `json:$[0].name`

## Follow a Debian bug activity

- Use this URL: `https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=<bug number>`
- Add in *Remove elements* ("filters and triggers" tab): `address`
