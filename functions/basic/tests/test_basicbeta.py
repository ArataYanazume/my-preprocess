"""
モジュールテスト
"""
import pytest
from functions.basic import (
    BasicBeta,
    basic_beta,
    beta_exp,
    beta_variance,
    beta_mode
)

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# ベータ関数
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1,param2,expected",
    [
        (2, 20, 0.002380952380952381),
    ],
)
def test_basic_beta(
        param1: int,
        param2: int,
        expected: float
    ) -> None:
    """
    ベータ関数
    """
    assert basic_beta(param1, param2) == expected

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# ベータ関数（クラス）
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1,param2",
    [
        (2, 20),
    ],
)
def test_basic_beta_class(
        param1: int,
        param2: int
    ) -> None:
    """
    ベータ関数（クラス）
    """
    test_beta = BasicBeta(param1, param2)
    assert test_beta() == basic_beta(param1, param2)
    assert test_beta.exp() == beta_exp(param1, param2)
    assert test_beta.mode() == beta_mode(param1, param2)

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# ベータ分布の期待値
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1,param2,expected",
    [
        (2, 20, 0.09090909090909091),
    ],
)
def test_beta_exp(
        param1: int,
        param2: int,
        expected: float
    ) -> None:
    """
    ベータ分布の期待値
    """
    assert beta_exp(param1, param2) == expected

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# ベータ分布の分散
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1,param2,expected",
    [
        (2, 20, 1.9008264462809918),
    ],
)
def test_beta_variance(
        param1: int,
        param2: int,
        expected: float
    ) -> None:
    """
    ベータ分布の分散
    """
    assert beta_variance(param1, param2) == expected

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
# ベータ分布のモード
#----------------------------------------------------------------------#
@pytest.mark.parametrize(
    "param1,param2,expected",
    [
        (2, 20, 0.05),
    ],
)
def test_beta_mode(
        param1: int,
        param2: int,
        expected: float
    ) -> None:
    """
    ベータ分布のモード
    """
    assert beta_mode(param1, param2) == expected
