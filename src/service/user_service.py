import requests
from src.config.config import Config as cf
import json

_host = cf.HOST + ":" + cf.PORT
_url = _host + "/api/users"
_headers = {"content-type": "application/json"}


def update_user(id_user, data_user:dict):
    uri = _url + f"/update-user/{id_user}"
    resp = requests.put(uri, data = json.dumps(data_user), headers=_headers)
    rs = json.loads(resp.content.decode('utf-8'))
    return {"status": resp.status_code, "message": rs}



if __name__=="__main__":
    data_user = {"idn": 132456734, "name": "Phuong", "wallet": 100000}
    resp = update_user(7, data_user=data_user)
    print(resp)
    
    

    

