"""
モジュールテスト
"""
import pytest
from functions.gradient import (
    relu,
)

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# OR回路
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1,expected",
    [
        (-1.0, 0.0),
        (-0.1, 0.0),
        (0.0, 0.0),
        (0.1, 0.1),
        (1.0, 1.0),
        (1.1, 1.1),
        (-1, 0.0),
        (0, 0.0),
        (1, 1.0),
    ],
)
def test_relu(
    param1: float, expected: float
    ) -> None:
    """ OR回路 """
    assert relu(param1) == expected
