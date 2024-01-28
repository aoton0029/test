from sqlalchemy import Engine, event
from sqlalchemy.orm import Session

# @event.listens_for(Engine, 'before_execute', retval=True)
# def before_execute(conn, clauseelement, multiparams, params):
#     print("Before Execute Event")

# @event.listens_for(Engine, 'after_execute', retval=True)
# def after_execute(conn, clauseelement, multiparams, params, result):
#     print("After Execute Event")

# @event.listens_for(Engine, 'engine_connect')
# def engine_connect(conn, branch):
#     print("Engine Connect Event")

# @event.listens_for(Engine, 'handle_error')
# def handle_error(exception_context):
#     print("Handle Error Event")

# @event.listens_for(Session, 'after_commit')
# def after_commit_listener(session):
#     print("Transaction committed!")
   

# # データベースに接続した際のイベント
# event.listen(engine, 'connect', identifier='connect_event')

# # トランザクションの開始時のイベント
# event.listen(session, 'begin', identifier='begin_event')

# @event.listens_for(session, 'before_cursor_execute', named=True)
# def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
#     print("Before cursor execute event")

# @event.listens_for(session, 'after_cursor_execute', named=True)
# def after_cursor_execute(conn, cursor, statement, parameters, context, executemany):
#     print("After cursor execute event")


# # データベースから切断した際のイベント
# event.listen(engine, 'disconnect', identifier='disconnect_event')

# # イベントを捕捉するリスナー
# def my_listener(target, connection, **kw):
#     print(f"Event detected on {target.__class__.__name__}")

# # テーブルにリスナーを追加
# event.listen(table, 'before_create', my_listener)

# # エンジンにリスナーを追加
# event.listen(engine, 'before_cursor_execute', my_listener)

# # セッションにリスナーを追加
# event.listen(metadata, 'after_flush', my_listener)

# # セッションにリスナーを追加 (セッション自体が対象)
# event.listen(metadata, 'after_flush', my_listener, propagate=True, target='session')