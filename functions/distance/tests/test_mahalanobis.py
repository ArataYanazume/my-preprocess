"""
モジュールテスト
"""
import numpy as np
import pytest
from functions.distance import (
    mahalanobis_distance
)

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# マハラノビス距離
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1, param2, param3, expected",
    [
        (
            np.array([1, 1, 1]),
            np.array([1,-1,-1]),
            [[1, 0.5, 0.5], [0.5, 1, 0.5], [0.5, 0.5, 1]],
            2.828,
        ),
    ],
)
def test_mahalanobis_distance(
        param1: np.ndarray,
        param2: np.ndarray,
        param3: np.ndarray,
        expected: np.ndarray
    ) -> None:
    """ マハラノビス距離 """
    data = mahalanobis_distance(param1, param2, param3, decimals=3)
    assert (data == expected).all()
