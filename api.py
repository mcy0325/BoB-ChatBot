from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from auth import api_key_auth
from ioc import vt_search
import schema
import crud
import logging
from database import db
from sqlalchemy import text
import hashlib

app = FastAPI(dependencies=[Depends(api_key_auth)])

@app.get("/")
async def root():
    logging.info("root api run")
    return {"message": "Hello World"}

@app.post("/users/")
def post_create_user(user: schema.UserCreate, dbsession: Session = Depends(db.get_session)):
    # User Check
    new_user = crud.create_user(dbsession, user)
    # Return User
    return new_user

@app.post("/access/")
def log_access(data: schema.Access_Data, session: Session = Depends(db.get_session)):
    key = data.access_time.isoformat() + data.channel_id + data.user_id
    access_id = hashlib.sha256(key.encode()).hexdigest()
    return crud.update_access_log(access_id, data, session)

@app.post("/ioc/search", response_model=schema.IOCResponse)
def ioc_search(
    data: schema.IOCQuery,
    dbsession: Session = Depends(db.get_session)
):
    vt_result = vt_search(data.query, data.ioc_type)
    saved = crud.save_ioc_result(dbsession, data.query, data.ioc_type, vt_result)
    return saved