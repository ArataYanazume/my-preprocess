"""
二変量解析の関数
"""
import numpy as np

#----------------------------------------------------------------------#
# Functions
#----------------------------------------------------------------------#
def columns_mean(
        data: np.ndarray
    ) -> np.ndarray:
    """ 平均値(列方向) """
    return np.mean(data, axis=0)

def columns_median(
        data: np.ndarray
    ) -> np.ndarray:
    """ 中央値(列方向) """
    return np.median(data, axis=0)

def columns_standard(
        data: np.ndarray
    ) -> np.ndarray:
    """ 標準偏差(列方向) """
    return np.std(data, axis=0)

def columns_variance(
        data: np.ndarray
    ) -> np.ndarray:
    """ 分散(列方向) """
    return np.var(data, axis=0)

def covariance_matrix(
        data: np.ndarray
    ) -> np.ndarray:
    """ 分散共分散行列
    - numpy行列
    - バイアスあり（n-1）
    """
    covariance = np.cov(data, rowvar=False, ddof=1)
    return covariance

def correlation_matrix(
        data: np.ndarray
    ) -> np.ndarray:
    """ 相関行列
    - numpy行列
    - バイアスあり（n-1）
    """
    corrcoef = np.corrcoef(data)
    return corrcoef
