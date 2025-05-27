"""
モジュールテスト
"""
import numpy as np
import pytest
from functions.basic import (
    covariance_matrix
)

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# 分散共分散行列
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1, expected",
    [
        (
            np.array([[ 1, 2, 3],[ 4, 5, 6],[ 7, 8, 9]]),
            np.array([[ 9, 9, 9],[ 9, 9, 9],[ 9, 9, 9]])
        ),
        (
            np.array([[ 1, 2, 3],[ 2, 4, 6],[ 3, 6, 9]]),
            np.array([[ 1, 2, 3],[ 2, 4, 6],[ 3, 6, 9]])
        ),
    ],
)
def test_covariance_matrix(
        param1: np.ndarray,
        expected: np.ndarray
    ) -> None:
    """ 分散共分散行列 """
    data = covariance_matrix(param1)
    assert data.all() == expected.all()
