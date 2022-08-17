import pytest


# this fixture will be used in tests, it does high level stuff.
# but it needs to be configurable by individual tests (or at least, files)
# and in some cases, we cannot make the fixture return a function/class easily,
# in particular when there are multiple fixture layers.
# so we depend here on a non-existing fixture, which will be defined at a later point.
@pytest.fixture()
def high_level_fixture(low_level_fixture):
    return low_level_fixture.upper()


# in this simple case, it could have been written as:
#
# @pytest.fixture()
# def high_level_fixture():
#     def process(value):
#         return value.upper()
#     return process

# and a test would have looked like:
#
# def test_upper_foo(high_level_fixture):
#     assert high_level_fixture("foo") == "FOO"

# but it's not always that simple
