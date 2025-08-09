import hashlib
import json
import base64
import os
from passlib.context import CryptContext
from sqlalchemy.orm import Session
# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to hash a password
def hash_password(password: str) -> tuple:
    # 솔트 생성 (16바이트)
    salt = os.urandom(16)
    # PBKDF2 해싱 (SHA256, 100,000회 반복)
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    # Base64 인코딩 (저장 용이하게)
    salt_b64 = base64.b64encode(salt).decode('utf-8')
    hashed_b64 = base64.b64encode(hashed).decode('utf-8')
    return salt_b64, hashed_b64

def verify_password(password: str, salt_b64: str, hashed_b64: str) -> bool:
    # Base64 디코딩
    salt = base64.b64decode(salt_b64)
    hashed_original = base64.b64decode(hashed_b64)
    # 입력 비밀번호 해싱
    hashed_check = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return hashed_check == hashed_original

import models
import schema
from config import conf

# Update User

# Find user

def create_user(db: Session, user: schema.UserCreate) -> models.User:
    salt_b64, hashed_b64 = hash_password(user.password)

    new_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_b64,
        salt=salt_b64
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

def update_access_log(access_id: str, access_item: schema.Access_Data, db: Session):
    log = models.AccessLog(
        access_id=access_id,
        user_id=access_item.user_id,
        channel_id=access_item.channel_id,
        access_time=access_item.access_time
    )

    db.add(log)
    db.commit()
    db.refresh(log)

    return log

def save_ioc_result(db: Session, query: str, ioc_type: str, result: dict) -> dict:
    ioc = models.IOCTable(
        query=query,
        ioc_type=ioc_type,
        result=json.dumps(result)  
    )
    db.add(ioc)
    db.commit()
    db.refresh(ioc)
    return {
        "id": ioc.id,
        "query": ioc.query,
        "ioc_type": ioc.ioc_type,
        "result": json.loads(ioc.result),  
        "scanned_at": ioc.scanned_at
    }

def get_ioc_by_query(db: Session, query: str):
    return db.query(models.IOCTable).filter(models.IOCTable.query == query).first()