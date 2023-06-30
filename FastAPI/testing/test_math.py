import pytest
from math import add, sub


def test_add():
    assert 1 + 1 == 2


def test_sub():
    assert 5 - 2 == 3


if __name__ == "__main__":
    pytest.main()