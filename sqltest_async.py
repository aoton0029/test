from sqlalchemy import create_engine, Column, Integer, String, Sequence, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, selectinload
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
import asyncio

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# データベースエンジンの作成
path = './test.db'
# SQLiteデータベースに接続するための非同期エンジンを作成
DATABASE_URL = "sqlite+aiosqlite:///./test.db"
engine = create_async_engine(DATABASE_URL, echo=True)

# セッションファクトリを作成
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
)

async def get_user(session, user_id):
    async with session() as async_session:
        statement = select(User).where(User.id == user_id)
        result = await async_session.execute(statement)
        user = result.scalar()
        return user

async def main():
    async with async_session() as session:
        user = await get_user(session, user_id=1)
        print(user.name, user.age)
