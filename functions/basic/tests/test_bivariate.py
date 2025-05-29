"""
モジュールテスト
"""
import numpy as np
import pytest
from functions.basic import (
    columns_mean,
    columns_median,
    columns_standard,
    columns_variance,
    covariance_matrix,
    correlation_matrix
)

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# 平均(列方向)
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1, expected",
    [
        (
            np.array([[1,2,3],[4,5,6],[7,8,9]]),
            np.array([4,5,6])
        ),
    ],
)
def test_columns_mean(
        param1: np.ndarray,
        expected: np.ndarray
    ) -> None:
    """ 平均(列方向) """
    data = columns_mean(param1)
    assert (data == expected).all()

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# 中央値(列方向)
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1, expected",
    [
        (
            np.array([[1,2,3],[4,5,6],[7,8,9]]),
            np.array([4,5,6])
        )
    ],
)
def test_columns_median(
        param1: np.ndarray,
        expected: np.ndarray
    ) -> None:
    """ 中央値(列方向) """
    data = columns_median(param1)
    assert (data == expected).all()

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# 標準偏差(列方向)
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1, expected",
    [
        (
            np.array([[1,2,3],[4,5,6],[7,8,9]]),
            np.array([2.449,2.449,2.449])
        ),
    ],
)
def test_columns_standard(
        param1: np.ndarray,
        expected: np.ndarray
    ) -> None:
    """ 標準偏差(列方向) """
    data = columns_standard(param1)
    assert (data.round(3) == expected).all()

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# 分散(列方向)
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1, expected",
    [
        (
            np.array([[1,2,3],[4,5,6],[7,8,9]]),
            np.array([6,6,6])
        )
    ],
)
def test_columns_variance(
        param1: np.ndarray,
        expected: np.ndarray
    ) -> None:
    """ 分散(列方向) """
    data = columns_variance(param1)
    assert (data.round(3) == expected).all()

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
    assert (data == expected).all()

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# 相関行列
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1, expected",
    [
        (
            np.array([[ 1, 2, 3],[ 4, 5, 6],[ 7, 8, 9]]),
            np.array([[ 1, 1, 1],[ 1, 1, 1],[ 1, 1, 1]])
        )
    ],
)
def test_correlation_matrix(
        param1: np.ndarray,
        expected: np.ndarray
    ) -> None:
    """ 相関行列 """
    data = correlation_matrix(param1)
    assert (data == expected).all()
