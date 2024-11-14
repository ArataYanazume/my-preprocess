"""
回路処理の関数
"""
import numpy as np

def orGate(x1, x2) -> int:
    """ OR回路 """
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    if np.sum(w*x) + b <= 0:
        return 0
    return 1

def andGate(x1, x2) -> int:
    """ AND回路 """
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    if np.sum(w*x) + b <= 0:
        return 0
    return 1

def nandGate(x1, x2) -> int:
    """ NAND回路 """
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    if np.sum(w*x) + b <= 0:
        return 0
    return 1

def xorGate(x1, x2) -> int:
    """ XOR回路 """
    s1 = nandGate(x1, x2)
    s2 = orGate(x1, x2)
    y = andGate(s1, s2)
    return y
