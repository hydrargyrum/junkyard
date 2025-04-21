#!/bin/sh -eu

: ${DOCKER:=docker}

$DOCKER run --rm -i docker.io/alpine:3 sh -c "apk add openssh >&2 && ssh-keygen -A >&2 && sshd -T" | sort > sshd-default-alpine.conf
$DOCKER run --rm -i docker.io/debian:sid sh -c "apt update >&2 && DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends openssh-server >&2  && sshd -T" | sort > sshd-default-debian-sid.conf
