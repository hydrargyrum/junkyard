
import os


__all__ = ("walk_no_xdev",)


def walk_no_xdev(top, onerror=None, followlinks=False):
    """Wraps os.walk() but doesn't enter mountpoints/other filesystems.

    This is like find's `-xdev` option or rsync's `--one-file-system` option.
    """

    # ignore "topdown" argument since it doesn't allow skipping dirs.

    # stores the device number of the root
    # so we later ensure we stay on same device.
    topdev = os.stat(top).st_dev

    # call os.walk() as usual
    for curpath, dirnames, filenames in os.walk(
            top, onerror=onerror, followlinks=followlinks,
    ):
        # prunes directories that are on a different device.
        # they will not be walked recursively.
        # os.walk() uses the list it returns, so we must modify it in-place
        # with "[:]"
        dirnames[:] = [
            dirname
            for dirname in dirnames
            if os.stat(os.path.join(curpath, dirname)).st_dev == topdev
        ]

        yield curpath, dirnames, filenames


# this can't be implemented for Path.rglob() because it doesn't allow
# skipping dirs.
