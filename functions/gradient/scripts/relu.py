"""
ReLU関数
"""
import numpy as np

def relu(
    x: float
    ) -> float:
    """ ReLU関数 """
    return float(np.maximum(0, x))

