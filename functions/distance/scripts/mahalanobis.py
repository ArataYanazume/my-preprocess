"""
マハラノビス距離
"""
import numpy as np

#----------------------------------------------------------------------#
# Functions
#----------------------------------------------------------------------#
def mahalanobis_distance(
        x: np.ndarray,
        y: np.ndarray,
        sigma: np.ndarray,
        decimals: int=1
    ) -> np.ndarray:
    """ マハラノビス距離 """
    matrix = np.linalg.inv(sigma)
    distance = (
        np.sqrt((x-y).T @ matrix @ (x-y))
        ).round(decimals)
    return distance

