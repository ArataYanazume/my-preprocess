"""
一変量解析の関数
"""
import numpy as np

#----------------------------------------------------------------------#
# Functions
#----------------------------------------------------------------------#
def uni_mean(
        data: np.ndarray
    ) -> np.ndarray:
    """
    平均(行方向)
    """
    return np.mean(data, axis=1)

def uni_median(
        data: np.ndarray
    ) -> np.ndarray:
    """
    中央値(行方向)
    """
    return np.median(data, axis=1)

def uni_standard(
        data: np.ndarray
    ) -> np.ndarray:
    """
    標準偏差(行方向)
    """
    return np.std(data, axis=1)

def uni_variance(
        data: np.ndarray
    ) -> np.ndarray:
    """
    分散(行方向)
    """
    return np.var(data, axis=1)
