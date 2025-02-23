"""
メッセージ出力の関数
"""
import logging
logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def log_info(message: str) -> None:
    """ 通常メッセージ """
    logger.info(message)
    print(f'[INFO] {message}')

def log_warn(message: str) -> None:
    """ 警告メッセージ """
    logger.warning(message)
    print(f'[WARNING] {message}')

def log_error(message: str) -> None:
    """ エラーメッセージ """
    logger.error(message)
    print(f'[ERROR] {message}')
