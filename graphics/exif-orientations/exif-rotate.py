#!/usr/bin/env python3
# SPDX-License-Identifier: WTFPL

# /// script
# dependencies = ["pyexiv2"]
# ///

import sys

import pyexiv2

image = pyexiv2.ImageMetadata(sys.argv[1])
image.read()

image['Exif.Image.Orientation'] = int(sys.argv[2])
image.write()
