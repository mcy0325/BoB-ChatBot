from fastapi import Header, HTTPException, Depends
from config import conf

def api_key_auth(api_key: str = Header(...)):
    if api_key != conf["api_key"]: 
        raise HTTPException(status_code=403, detail="Invalid API Key")
