"""
モジュールテスト
"""
import inspect
from unittest import TestCase
from functions.char import (
    shift,
    text_if_end_with,
    text_if_start_with,
    text_join,
    text_reprace,
    text_search,
    text_strip,
    text_to_list,
    text_upper,
    text_abs,
    text_ceil,
    text_float,
    text_floor
)
from functions.print_log import log_info

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
class TestChar(TestCase):
    """ ユニットテスト """

    def setUp(self):
        """ ユニットテスト開始 """
        log_info('Test Char: setUp')

    def tearDown(self):
        """ ユニットテスト終了 """
        log_info('Test Char: tearDown')

    def test_shift1(self):
        """ 文字シフト
        開始位置：指定
        終了位置：指定
        """
        log_info(inspect.currentframe().f_code.co_name)
        text = 'Hello World'
        self.assertEqual(
            shift(text, 1, 3),
            'ell'
        )

    def test_shift2(self):
        """ 文字シフト
        開始位置：未指定
        終了位置：指定
        """
        log_info(inspect.currentframe().f_code.co_name)
        text = 'Hello World'
        self.assertEqual(
            shift(text, 0, 5),
            'Hello'
        )

    def test_shift3(self):
        """ 文字シフト
        開始位置：指定
        終了位置：未指定
        """
        log_info(inspect.currentframe().f_code.co_name)
        text = 'Hello World'
        self.assertEqual(
            shift(text, 6),
            'World'
        )

    def test_text_if_end_with1(self):
        """ 終了文字のチェック
        正解
        """
        log_info(inspect.currentframe().f_code.co_name)
        self.assertTrue(text_if_end_with(
            text='Hello World',
            check='d'
        ))

    def test_text_if_end_with2(self):
        """ 終了文字のチェック
        不正解
        """
        log_info(inspect.currentframe().f_code.co_name)
        self.assertFalse(text_if_end_with(
            text='Hello World',
            check='H'
        ))

    def test_text_if_start_with1(self):
        """ 開始文字のチェック
        正解
        """
        log_info(inspect.currentframe().f_code.co_name)
        self.assertTrue(text_if_start_with(
            text='Hello World',
            check='H'
        ))

    def test_text_if_start_with2(self):
        """ 開始文字のチェック
        不正解
        """
        log_info(inspect.currentframe().f_code.co_name)
        self.assertFalse(text_if_start_with(
            text='Hello World',
            check='d'
        ))

    def test_text_join(self):
        """ テキスト結合 """
        log_info(inspect.currentframe().f_code.co_name)
        self.assertEqual(
            text_join(['Hello', ' ', 'World']),
            'Hello, ,World'
        )

    def test_text_reprace(self):
        """ 置換 """
        log_info(inspect.currentframe().f_code.co_name)
        self.assertEqual(
            text_reprace(
                'Herro World',
                'r',
                'l'
            ),
            'Hello Wolld'
        )

    def test_text_search1(self):
        """ テキスト中の文字のチェック
        ある場合
        """
        log_info(inspect.currentframe().f_code.co_name)
        self.assertTrue(
            text_search(
                'Hello World',
                'e'
        ))

    def test_text_search2(self):
        """ テキスト中の文字のチェック
        ない場合
        """
        log_info(inspect.currentframe().f_code.co_name)
        self.assertFalse(
            text_search(
                'Hello World',
                'a'
        ))

    def test_text_strip1(self):
        """ 半角スペース/指定文字の除去
        キーワード指定あり
        """
        log_info(inspect.currentframe().f_code.co_name)
        self.assertEqual(
            text_strip(
                text='Hello World',
                keyword='l'
            ),
            'Heo Word'
        )

    def test_text_strip2(self):
        """ 半角スペース/指定文字の除去
        キーワード指定なし
        """
        log_info(inspect.currentframe().f_code.co_name)
        self.assertEqual(
            text_strip(
                text='Hello World'
            ),
            'HelloWorld'
        )

    def test_text_to_list(self):
        """ 文字列のリスト化 """
        log_info(inspect.currentframe().f_code.co_name)
        self.assertEqual(
            text_to_list('Hello World'),
            (['Hello', 'World'])
        )

    def test_text_upper(self):
        """ 大文字 """
        log_info(inspect.currentframe().f_code.co_name)
        self.assertEqual(
            text_upper("string"),
            "STRING"
        )

class TestNumc(TestCase):
    """ ユニットテスト """

    def setUp(self):
        """ ユニットテスト開始 """
        log_info('Test Numc: setUp')

    def tearDown(self):
        """ ユニットテスト終了 """
        log_info('Test Numc: tearDown')

    def test_text_abs(self):
        """ 絶対値 """
        log_info(inspect.currentframe().f_code.co_name)
        self.assertEqual(
            text_abs(-4.2),
            '4.2'
        )

    def test_text_ceil(self):
        """ 小数点切り上げ """
        log_info(inspect.currentframe().f_code.co_name)
        self.assertEqual(
            text_ceil(5.4),
            '6'
        )

    def test_text_float1(self):
        """ 浮動小数点2桁
        元の型：整数(int)
        """
        log_info(inspect.currentframe().f_code.co_name)
        b = 100
        self.assertEqual(
            text_float(b),
            '100.00'
        )

    def test_text_float2(self):
        """ 浮動小数点2桁
        元の型：数値(float)
        """
        log_info(inspect.currentframe().f_code.co_name)
        c = 3.14159
        self.assertEqual(
            text_float(c),
            '3.14'
        )

    def test_text_floor(self):
        """ 小数点切り捨て """
        log_info(inspect.currentframe().f_code.co_name)
        self.assertEqual(
            text_floor(4.2),
            '4'
        )
