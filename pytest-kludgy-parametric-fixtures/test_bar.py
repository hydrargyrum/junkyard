import pytest


@pytest.fixture()
def low_level_fixture():
    return "bar"


# we depend on the high-level fixture
# and we configured it by defining the low-level fixture in this file.
# this low-level fixture will only apply to this file.
def test_upper_bar(high_level_fixture):
    return high_level_fixture == "BAR"
