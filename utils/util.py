from functools import wraps
import time
import logging

def log_stopwatch(logger:logging.Logger):
    def stopwatch(func):
        @wraps(func)
        def wrapper(*args, **kargs):
            # 処理開始直前の時間
            start = time.time()
            # 処理実行
            result = func(*args, **kargs)
            # 処理終了直後の時間から処理時間を算出
            elapsed_time = time.time() - start
            # 処理時間を出力
            logger.info("{} ms in {}".format(elapsed_time * 1000, func.__name__))
            return result
        return wrapper
    return stopwatch