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

# @app.route('/')
# def home():
#     return 'Hello, World!'

@app.route('/add')
def add():
    sqltest.insert_data()
    return {"Result" : "OK"}

async def heavy_processing():
    # 重い処理の代わりに非同期に待つ
    await asyncio.sleep(5)
    return "Processing complete"

@app.route("/")
async def read_root():
    port = request.access_route[0][1] if request.access_route else None
    ip = request.remote_addr
    print('start {2}:{3} [{0}] {1}'.format(datetime.datetime.now(), th.get_ident(), ip, port))
    result = await heavy_processing()
    #print('{2} [{0}] {1}'.format(datetime.datetime.now(), th.get_ident(), request.host))
    return {"message": result}

if __name__ == '__main__':
    app.run(debug=True)