"""
二変量解析の関数
"""
import numpy as np

#----------------------------------------------------------------------#
# Functions
#----------------------------------------------------------------------#
def covariance_matrix(
        X: np.ndarray
    ) -> np.ndarray:
    """ 分散共分散行列
    - numpy行列
    - バイアスあり（n-1）
    """
    covariance = np.cov(X, rowvar=False, ddof=1)
    return covariance
