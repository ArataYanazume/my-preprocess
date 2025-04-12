"""
モジュールテスト
"""
import pytest
from functions.gate import (
    or_gate,
    and_gate,
    nand_gate,
    xor_gate
)

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# OR回路
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1,param2,expected",
    [
        (0, 0, 0),
        (1, 0, 1),
        (0, 1, 1),
        (1, 1, 1),
    ],
)
def test_or_gate(
    param1: int, param2: int, expected: int
    ) -> None:
    """ OR回路 """
    assert or_gate(param1, param2) == expected

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# AND回路
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1,param2,expected",
    [
        (0, 0, 0),
        (1, 0, 0),
        (0, 1, 0),
        (1, 1, 1),
    ],
)
def test_and_gate(
    param1: int, param2: int, expected: int
    ) -> None:
    """ AND回路 """
    assert and_gate(param1, param2) == expected

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# NAND回路
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1,param2,expected",
    [
        (0, 0, 1),
        (1, 0, 1),
        (0, 1, 1),
        (1, 1, 0),
    ],
)
def test_nand_gate(
    param1: int, param2: int, expected: int
    ) -> None:
    """ NAND回路 """
    assert nand_gate(param1, param2) == expected

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# XOR回路
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1,param2,expected",
    [
        (0, 0, 0),
        (1, 0, 1),
        (0, 1, 1),
        (1, 1, 0),
    ],
)
def test_xor_gate(
    param1: int, param2: int, expected: int
    ) -> None:
    """ XOR回路 """
    assert xor_gate(param1, param2) == expected
