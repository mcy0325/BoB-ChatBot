from typing import Optional
from pydantic import BaseModel, EmailStr # pylint: disable=no-name-in-module
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
    
    model_config = {
        "from_attributes": True
    }

class Access_Data(BaseModel):
    user_id: str
    channel_id: str
    access_time: datetime

class IOCQuery(BaseModel):
    query: str  
    ioc_type: str 

class IOCResponse(BaseModel):
    id: int
    query: str
    ioc_type: str
    result: dict
    scanned_at: datetime

    model_config = {
        "from_attributes": True
    }