"""
回路処理の関数
"""
import numpy as np

def or_gate(x1, x2) -> int:
    """ OR回路 """
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    if np.sum(w*x) + b <= 0:
        return 0
    return 1

def and_gate(x1, x2) -> int:
    """ AND回路 """
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    if np.sum(w*x) + b <= 0:
        return 0
    return 1

def nand_gate(x1, x2) -> int:
    """ NAND回路 """
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    if np.sum(w*x) + b <= 0:
        return 0
    return 1

def xor_gate(x1, x2) -> int:
    """ XOR回路 """
    s1 = nand_gate(x1, x2)
    s2 = or_gate(x1, x2)
    y = and_gate(s1, s2)
    return y
