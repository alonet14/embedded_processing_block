import requests
from src.config.config import Config as cf

import json

_host = cf.HOST + ":" + cf.PORT

_url = _host + "/api/battery"


def find_all_battery():
    uri = _url + "/find-all-batteries"
    resp = requests.get(uri)
    rs = json.loads(resp.content.decode('utf-8'))
    return {"status": resp.status_code, "message": rs}


def find_battery_by_id(id):
    uri = _url + f'/{id}'
    resp = requests.get(uri, timeout=10)
    rs = json.loads(resp.content.decode('utf-8'))
    return {"status": resp.status_code, "message": rs}


def find_user_by_rfid(rfid):
    uri = _url + "/find-user-by-rfid"
    resp = requests.get(uri, timeout=1000, params={"code": rfid})
    rs = json.loads(resp.content.decode('utf-8'))
    return {"status": resp.status_code, "message": rs}


