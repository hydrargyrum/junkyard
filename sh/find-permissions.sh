#!/bin/false
# SPDX-License-Identifier: WTFPL

# small GNU find(1) snippets for dealing with permissions
# (can be ported to non-GNU find tools supporting `-or`)

###################
## executable files

# find executable files
find -type f -perm /100

# find non-executable files
find -type f -not -perm /100

##################
## non-owner write

# find files/folders writable by non-owner
find -perm /022

#################
## non-owner read

# find folders readable by non-owner
find -type d -perm /055

# find folders NOT readable by non-owner
find -type d -not -perm /055

# find files readable by non-owner
find -type f -perm /044

# find files NOT readable by non-owner
find -type f -not -perm /044
