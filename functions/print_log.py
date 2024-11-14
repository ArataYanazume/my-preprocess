"""
メッセージ出力の関数
"""

def log_info(message: str) -> None:
    """ 通常メッセージ """
    print(f'[INFO] {message}')

def log_warn(message: str) -> None:
    """ 警告メッセージ """
    print(f'[WARNING] {message}')

def log_error(message: str) -> None:
    """ エラーメッセージ """
    print(f'[ERROR] {message}')
