from concurrent.futures import ThreadPoolExecutor
import datetime
import pprint
import random
import traceback
import pandas as pd
import sqlalchemy
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine, event, text
from sqlalchemy.engine import Engine
from sqlalchemy.pool import Pool
import unittest
import logging
import sys
import os
from pathlib import Path
import importlib
sys.path.append(str(Path(__file__).parent.parent))
import utils
import asyncio

logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG)
utils.log.LoggerConfig.set_stream_handler(logger)

class MyTestCase(unittest.TestCase):
    WORK_NUM = 10
    def __init__(self, methodName: str = "runTest") -> None:
        self.path = 'testdb.db'

    def setUp(self):
        self.path = 'testdb.db'
    
    def create_test_data(self):      
        # データ生成のための関数
        def generate_data():
            data = []
            for _ in range(1000000):
                row = {
                    'col1': random.randint(1, 100),
                    'col2': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5)),
                    'col3': datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 365)),
                    'col4': random.randint(1, 100),
                    'col5': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5)),
                    'col6': datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 365)),
                    'col7': random.randint(1, 100),
                    'col8': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5)),
                    'col9': datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 365)),
                    'col10': random.randint(1, 100),
                }
                data.append(row)
            return data

        # DataFrameの作成
        df = pd.DataFrame(generate_data())
        # SQLiteメモリデータベースに書き込み
        engine = create_engine(f'sqlite:///{self.path}')
        df.to_sql('test_data', engine, index=False, if_exists='replace')
            
    def query(self, engine:Engine):
        sql = f'''
                SELECT * FROM test_data
                '''
        print(engine)
        with engine.connect() as con:
            try:
                df = pd.read_sql_query(text(sql), con)
                logger.info(len(df))
            except:
                logger.error(traceback.format_exc())
    

    # @utils.util.log_stopwatch(logger)
    # def test_single_thread(self):
    #     logger.info('test_single_thread')
    #     # SQLiteデータベースへの接続
    #     engine = create_engine(f'sqlite:///{self.path}')
    #     connect_args = engine.dialect.create_connect_args(engine.url)
    #     logger.info(connect_args)
    #     for _ in range(self.WORK_NUM):
    #             self.query(engine)

    @utils.util.log_stopwatch(logger)
    def test_multi_thread(self):
        logger.info('test_multi_thread')
        # スレッドモードの設定（"single", "multi", "serializable"のいずれか
        thread_mode = "multi"
        # SQLiteデータベースへの接続
        engine = create_engine(f'sqlite:///{self.path}', connect_args={'check_same_thread': False, 'thread_mode': thread_mode})
        connect_args = engine.dialect.create_connect_args(engine.url)
        logger.info(connect_args)
        with ThreadPoolExecutor(max_workers=self.WORK_NUM) as exec:
            ens = [engine for _ in range(self.WORK_NUM)]
            res = exec.map(self.query, ens)
            print(res)

    def test_multi_process(self):
        pass

    async def execute_query_async(self, query, db_path):
        logger.debug("")

    @utils.util.log_stopwatch(logger)
    async def main(self):
        # SQLiteデータベースファイルのパス
        db_path = "testdb.db"

        # SQLクエリのリスト
        queries = [
            "SELECT * FROM test_data",
            "SELECT * FROM test_data",
            "SELECT * FROM test_data",
        ]

        tasks = [self.execute_query_async(query, db_path) for query in queries]
        results = await asyncio.gather(*tasks)

        # 結果を表示
        for i, result in enumerate(results):
            logger.debug(f"Query {i + 1} result:")
