""""
テキスト処理の関数
"""
def shift(
    text: str,
    start: int = 0,
    interval: int = 0
    ) -> str:
    """ 開始位置から指定文字数の切り出し """
    if interval == 0:
        return text[start:]
    if start == 0:
        return text[:interval]
    return text[start:(start+interval)]

def text_if_end_with(
    text: str,
    check: str
    ) -> bool:
    """ 終了文字のチェック """
    return text.endswith(check)

def text_if_start_with(
    text: str,
    check: str
    ) -> bool:
    """ 開始文字のチェック """
    return text.startswith(check)

def text_join(
    data: list
    ) -> str:
    """ リストを文字列結合 """
    return ','.join(data)

def text_reprace(
    text: str,
    before: str,
    after: str
    ) -> str:
    """ 置換 """
    return text.replace(before, after)

def text_search(
    text: str,
    check: str
    ) -> bool:
    """ テキスト中の文字のチェック """
    return check in text

def text_strip(
    text: str,
    keyword:str = ' '
    ) -> str:
    """ 半角スペース/指定文字の除去 """
    return text.replace(keyword, '')

def text_to_list(
    text: str,
    keyword: str = ' '
    ) -> list:
    """ 文字列のリスト化 """
    return text.split(keyword)

def text_upper(
    text: str
    ) -> str:
    """ 大文字 """
    return text.upper()
