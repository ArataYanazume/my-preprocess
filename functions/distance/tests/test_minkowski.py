"""
モジュールテスト
"""
import numpy as np
import pytest
from functions.distance import (
    euclidean_distance,
    manhattan_distance,
)

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# ユークリッド距離
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1, param2, expected",
    [
        (
            np.array([1, 1, 1]),
            np.array([1,-1,-1]),
            2.828,
        ),
        (
            np.array([1, 1, 1]),
            np.array([-1,-1,-1]),
            3.464,
        ),
    ],
)
def test_euclidean_distance(
        param1: np.ndarray,
        param2: np.ndarray,
        expected: np.ndarray
    ) -> None:
    """
    ユークリッド距離
    """
    data = euclidean_distance(param1, param2, decimals=3)
    assert (data == expected).all()

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# マンハッタン距離
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1, param2, expected",
    [
        (
            np.array([1, 1, 1]),
            np.array([1,-1,-1]),
            4,
        ),
        (
            np.array([1, 1, 1]),
            np.array([-1,-1,-1]),
            6,
        ),
    ],
)
def test_manhattan_distance(
        param1: np.ndarray,
        param2: np.ndarray,
        expected: np.ndarray
    ) -> None:
    """
    マンハッタン距離
    """
    data = manhattan_distance(param1, param2, decimals=3)
    assert (data == expected).all()
