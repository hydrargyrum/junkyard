__all__ = ("merge_iterables",)


def merge_iterables(*iterables, key=lambda x: x):
    """Take multiple sorted iterables and create a single sorted iterator.

    `iterables` can be lists, tuples, but also generators, file descriptors.
    Each of them must be sorted individually, and you want to iterate on all
    of them in parallel, but keeping them sorted as a whole.
    The function is lazy and consumes elements only as needed.

    Optional `key` param is a callable to get the sort key from an element,
    like the `key` param of `min` or `sorted` builtins.
    """
    def keyfunc(kv):
        return key(kv[1])

    def consume(iterator):
        try:
            value = next(iterator)
        except StopIteration:
            del iterables[iterator]
        else:
            iterables[iterator] = value

    iterables = {iter(it): None for it in iterables}
    for iterator in list(iterables):
        consume(iterator)

    while iterables:
        iterator, value = min(iterables.items(), key=keyfunc)
        yield value
        consume(iterator)


def test_merge():
    expected = [1.0, 1, 1.5, 2, 3, 25, 100]
    assert list(merge_iterables([1.0,2,25], [1,1.5,3], [100], [])) == expected


def test_stable():
    a = 1
    b = 1.0
    assert a is not b

    new = list(merge_iterables([a], [b]))
    assert new[0] is a
    assert new[1] is b

    new = list(merge_iterables([b], [a]))
    assert new[0] is b
    assert new[1] is a


def test_lazy():
    def infinite(n=0):
        while True:
            yield n
            n += 1

    it = merge_iterables(infinite(), infinite(1.5))
    expected_list = [0, 1, 1.5, 2, 2.5, 3, 3.5]
    for expected, got in zip(expected_list, it):
        assert expected == got
