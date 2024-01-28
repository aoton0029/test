from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import time

# SQLAlchemyモデルの定義
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# データベースエンジンの作成
path = './test.db'
engine = create_engine(f'sqlite:///{path}')

# モデルをデータベースに反映
Base.metadata.create_all(engine)

# セッションの作成
Session = scoped_session(sessionmaker(bind=engine))

# IOバウンドな操作の例: データベースにデータを挿入する
def insert_data():
    with Session() as ses:
        for i in range(1, 10001):
            user = User(name=f'User{i}', age=i)
            ses.add(user)
        ses.commit()

# IOバウンドな操作の例: データベースからデータを取得する
def retrieve_data():
    with Session() as ses:
        users = ses.query(User).all()
        return len(users)
        # for user in users:
        #     print(f'User ID: {user.id}, Name: {user.name}, Age: {user.age}')
