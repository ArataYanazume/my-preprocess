"""
ミンコフスキー距離
"""
import numpy as np

#----------------------------------------------------------------------#
# Functions
#----------------------------------------------------------------------#
def euclidean_distance(
        x: np.ndarray,
        y: np.ndarray,
        decimals: int=1
    ) -> np.ndarray:
    """
    ユークリッド距離
    """
    distance = (
        np.sqrt(np.sum((x-y)**2))
        ).round(decimals)
    return distance

def manhattan_distance(
        x: np.ndarray,
        y: np.ndarray,
        decimals: int=1
    ) -> np.ndarray:
    """
    マンハッタン距離 """
    distance = (
        np.sum(abs(x-y))
        ).round(decimals)
    return distance
