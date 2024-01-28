import datetime
import time
from flask import Flask, request
import asyncio
# from quart import Quart, request
import os
import threading as th
from waitress import serve
import sqltest

app = Flask(__name__)

@app.route('/add')
def add():
    sqltest.insert_data()
    return {"Result" : "OK"}

def heavy_processing():
    # 重い処理の代わりに非同期に待つ
    sqltest.retrieve_data()
    return "Processing complete"

@app.route("/")
def read_root():
    port = request.access_route[0][1] if request.access_route else None
    ip = request.remote_addr
    print('start {1} {2}:{3} [{0}]'.format(datetime.datetime.now(), th.get_ident(), ip, port))
    result = heavy_processing()
    print('end {1} {2}:{3} [{0}]'.format(datetime.datetime.now(), th.get_ident(), ip, port))
    return {"message": result}

if __name__ == '__main__':
    app.run(debug=True)