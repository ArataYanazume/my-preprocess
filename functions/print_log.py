"""
メッセージ出力の関数
"""

def log_info(message: str) -> None:
    print(f'[INFO] {message}')

def log_warn(message: str) -> None:
    print(f'[WARNING] {message}')

def log_error(message: str) -> None:
    print(f'[ERROR] {message}')
