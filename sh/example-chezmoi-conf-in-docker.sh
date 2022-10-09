#!/bin/sh -e
# use a container but miss your carefully crafted dotfiles?
# if you use chezmoi, it's easy

TMPDIR=${TMPDIR:-/tmp}
d=$(mktemp -d "$TMPDIR/chezmoi-docker.XXXXXX")

# create a copy of the dotfiles in a temp directory
chezmoi archive | tar -x -C "$d"

# mount the temp directory as ~root so root has all the dotfiles
# and start the container
docker run -it -v "$d:/root" debian:stable bash

# alternatively, to copy dotfiles to an already running container:
#  chezmoi archive | docker exec -u root -w /root -i CONTAINER_ID tar xf -

# or (if not using root user in the container):
#  chezmoi archive | docker exec -u foo -w /home/foo -i CONTAINER_ID tar xf -
