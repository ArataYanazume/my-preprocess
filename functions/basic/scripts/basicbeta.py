"""
ベータ分布・ベータ関数
"""
import math

#----------------------------------------------------------------------#
# Class
#----------------------------------------------------------------------#
# ベータ分布・ベータ関数
#----------------------------------------------------------------------#
class BasicBeta:
    """ ベータ分布・ベータ関数 """
    def __init__(self, a, b) -> None:
        """ ベータ分布・ベータ関数 """
        self.a = a
        self.b = b

    def __call__(self) -> float:
        """ call function """
        a = self.a
        b = self.b
        return math.gamma(a) * math.gamma(b) / math.gamma(a + b)

    def exp(self) -> float:
        """ 期待値 """
        return self.a / (self.a + self.b)

    def variance(self) -> float:
        """ 分散 """
        return ((self.a * self.b) /
                (self.a + self.b)**2 * (self.a + self.b + 1))

    def mode(self) -> float:
        """ モード """
        return (self.a - 1) / (self.a + self.b - 2)


#----------------------------------------------------------------------#
# Fanctions
#----------------------------------------------------------------------#
def basic_beta(a, b):
    """ ベータ関数 """
    return BasicBeta(a, b)()

def beta_exp(a, b) -> float:
    """ 期待値 """
    beta = BasicBeta(a, b)
    return beta.a / (beta.a + beta.b)

def beta_variance(a, b) -> float:
    """ 期待値 """
    return BasicBeta(a, b).variance()

def beta_mode(a, b) -> float:
    """ モード """
    beta = BasicBeta(a, b)
    return (beta.a - 1) / (beta.a + beta.b - 2)
