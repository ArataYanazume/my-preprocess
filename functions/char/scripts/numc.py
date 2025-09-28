""""
テキスト処理の関数
"""
from math import ceil, floor

def text_abs(
    num: float
    ) -> str:
    """
    絶対値
    """
    return f'{abs(num)}'

def text_ceil(
    num: float
    ) -> str:
    """
    小数点切り上げ
    """
    return f'{ceil(num)}'

def text_float(
    num: float
    ) -> str:
    """
    数値を浮動小数点下2桁のテキストに変換
    """
    return f'{num:.2f}'

def text_floor(
    num: float
    ) -> str:
    """
    小数点切り捨て
    """
    return f'{floor(num)}'
