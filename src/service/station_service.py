import requests
from src.config.config import Config as cf
import json

_host = cf.HOST + ":" + cf.PORT
_url = _host + "/api/station"
_headers = {"content-type": "application/json"}

def find_station(id):
    uri = _url + f'/{id}'
    resp = requests.get(uri, timeout=10)
    rs = json.loads(resp.content.decode('utf-8'))
    return {"status": resp.status_code, "message": rs}

if __name__=="__main__":
    print(find_station(1))