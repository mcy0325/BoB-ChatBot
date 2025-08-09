import base64
import requests
from config import conf

VT_API_KEY = conf["api_key"]
headers = {"x-apikey": VT_API_KEY}

def encode_url(url: str) -> str:
    return base64.urlsafe_b64encode(url.encode()).decode().strip("=")

def vt_search(query: str, ioc_type: str) -> dict:
    if ioc_type == "url":
        object_id = encode_url(query)
        endpoint = f"https://www.virustotal.com/api/v3/urls/{object_id}"
    elif ioc_type == "ip_address":
        endpoint = f"https://www.virustotal.com/api/v3/ip_addresses/{query}"
    elif ioc_type == "domain":
        endpoint = f"https://www.virustotal.com/api/v3/domains/{query}"
    elif ioc_type == "file":
        endpoint = f"https://www.virustotal.com/api/v3/files/{query}"
    else:
        raise ValueError("Unsupported IoC type")
    
    res = requests.get(endpoint, headers=headers)
    return res.json()
