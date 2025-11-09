"""
モジュールテスト
"""
import pytest
import numpy as np
from functions.gradient import (
    relu,
    relu_gradient,
    leaky_relu,
)

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# ReLU関数
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1,expected",
    [
        (np.array([-1.0]), np.array([0.0])),
        (np.array([-0.1]), np.array([0.0])),
        (np.array([0.0]), np.array([0.0])),
        (np.array([0.1]), np.array([0.1])),
        (np.array([1.0]), np.array([1.0])),
        (np.array([1.1]), np.array([1.1])),
        (np.array([-1]), np.array([0.0])),
        (np.array([0]), np.array([0.0])),
        (np.array([1]), np.array([1.0])),
        (
            np.array([-1.0, -0.1, 0.0, 0.1, 1.0, 1.1]),
            np.array([0.0, 0.0, 0.0, 0.1, 1.0, 1.1])),
        (
            np.array([[-1.0], [-0.1], [0.0], [0.1], [1.0], [1.1]]),
            np.array([[0.0], [0.0], [0.0], [0.1], [1.0], [1.1]])),
    ],
)
def test_relu(
        param1: np.ndarray,
        expected: np.ndarray
    ) -> None:
    """ ReLU関数 """
    assert (relu(param1) == expected).all()

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# ReLU関数の勾配
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1,expected",
    [
        (np.array([-1.0]), np.array([0.0])),
        (np.array([-0.1]), np.array([0.0])),
        (np.array([0.0]), np.array([0.0])),
        (np.array([0.1]), np.array([1.0])),
        (np.array([1.0]), np.array([1.0])),
        (np.array([1.1]), np.array([1.0])),
        (np.array([-1]), np.array([0.0])),
        (np.array([0]), np.array([0.0])),
        (np.array([1]), np.array([1.0])),
        (
            np.array([-1.0, -0.1, 0.0, 0.1, 1.0, 1.1]),
            np.array([0.0, 0.0, 0.0, 1.0, 1.0, 1.0])),
        (
            np.array([[-1.0], [-0.1], [0.0], [0.1], [1.0], [1.1]]),
            np.array([[0.0], [0.0], [0.0], [1.0], [1.0], [1.0]])),
    ],
)
def test_relu_gradient(
        param1: np.ndarray,
        expected: np.ndarray
    ) -> None:
    """ ReLU関数の勾配 """
    assert (relu_gradient(param1) == expected).all()

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# Leaky ReLU関数
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1,alpha,expected",
    [
        (np.array([-1.0]), 0.01, np.array([-0.01])),
        (np.array([-0.1]), 0.01, np.array([-0.001])),
        (np.array([0.0]), 0.01, np.array([0.0])),
        (np.array([0.1]), 0.01, np.array([0.1])),
        (np.array([1.0]), 0.01, np.array([1.0])),
        (np.array([1.1]), 0.01, np.array([1.1])),
        (np.array([-1.0]), 0.1, np.array([-0.1])),
        (np.array([-0.1]), 0.1, np.array([-0.01])),
        (np.array([0.0]), 0.1, np.array([0.0])),
        (np.array([0.1]), 0.1, np.array([0.1])),
        (np.array([1.0]), 0.1, np.array([1.0])),
        (np.array([1.1]), 0.1, np.array([1.1])),
    ],
)
def test_leaky_relu(
        param1: np.ndarray,
        alpha: float,
        expected: np.ndarray
    ) -> None:
    """ Leaky ReLU関数 """
    assert (leaky_relu(param1, alpha) == expected).all()
