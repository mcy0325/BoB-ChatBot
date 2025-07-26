from sqlalchemy import Column, DateTime, JSON, Integer, String, Text
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = 'UserTable'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)
    salt = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now)

class AccessLog(Base):
    __tablename__ = 'AccessLogTable'

    id = Column(Integer, primary_key=True, autoincrement=True)
    access_id = Column(String(64), unique=True)
    user_id = Column(String(50), nullable=False)
    channel_id = Column(String(50), nullable=False)
    access_time = Column(DateTime, nullable=False)

class IOCTable(Base):
    __tablename__ = "IOCTable"

    id = Column(Integer, primary_key=True, index=True)
    query = Column(String(256), nullable=False) 
    result = Column(JSON, nullable=False)       
    ioc_type = Column(String(50), nullable=False) 
    scanned_at = Column(DateTime, default=datetime.utcnow)
