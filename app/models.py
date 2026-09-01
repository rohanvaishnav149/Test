from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column,String,Integer,Float

class Base(DeclarativeBase):
        pass

#table 1---users

class Users(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age=Column(Integer)
    email = Column(String(100), unique=True, nullable=False)

