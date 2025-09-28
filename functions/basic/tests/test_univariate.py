"""
モジュールテスト
"""
import numpy as np
import pytest
from functions.basic import (
    uni_mean,
    uni_median,
    uni_standard,
    uni_variance
)

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# 平均(行方向)
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1, expected",
    [
        (
            np.array([[1,2,3],[4,5,6],[7,8,9]]),
            np.array([2,5,8])
        ),
    ],
)
def test_uni_mean(
        param1: np.ndarray,
        expected: np.ndarray
    ) -> None:
    """
    平均(行方向)
    """
    data = uni_mean(param1)
    assert (data == expected).all()

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# 中央値(行方向)
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1, expected",
    [
        (
            np.array([[1,2,3],[4,5,6],[7,8,9]]),
            np.array([2,5,8])
        )
    ],
)
def test_uni_median(
        param1: np.ndarray,
        expected: np.ndarray
    ) -> None:
    """
    中央値(行方向)
    """
    data = uni_median(param1)
    assert (data == expected).all()

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# 標準偏差(行方向)
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1, expected",
    [
        (
            np.array([[1,2,3],[4,5,6],[7,8,9]]),
            np.array([0.816,0.816,0.816])
        ),
    ],
)
def test_uni_standard(
        param1: np.ndarray,
        expected: np.ndarray
    ) -> None:
    """
    標準偏差(行方向)
    """
    data = uni_standard(param1)
    assert (data.round(3) == expected).all()

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# 分散(行方向)
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1, expected",
    [
        (
            np.array([[1,2,3],[4,5,6],[7,8,9]]),
            np.array([0.667,0.667,0.667])
        )
    ],
)
def test_uni_variance(
        param1: np.ndarray,
        expected: np.ndarray
    ) -> None:
    """
    分散(行方向)
    """
    data = uni_variance(param1)
    assert (data.round(3) == expected).all()
