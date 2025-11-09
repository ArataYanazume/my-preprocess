"""
ReLU関数
"""
import numpy as np

def relu(
    x: np.ndarray
    ) -> np.ndarray:
    """
    ReLU関数
    """
    return np.maximum(0, x)


def relu_gradient(
    x: np.ndarray
    ) -> np.ndarray:
    """
    ReLU関数の勾配
    - x > 0 : 1
    - x <= 0 : 0
    """
    return np.where(x > 0, 1.0, 0.0)


def leaky_relu(
    x: np.ndarray,
    alpha: float = 0.01
    ) -> np.ndarray:
    """
    Leaky ReLU関数
    """
    return np.where(x > 0, x, alpha * x).round(4)
