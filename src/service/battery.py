import requests
from src.config.config import Config as cf
from configparser import ConfigParser

import json

config = ConfigParser()
host = cf.HOST + ":" + cf.PORT

url = host + "/api/battery"


def find_all_battery():
    uri = url + "/find-all-batteries"
    resp = requests.get(uri)
    rs = json.loads(resp.content.decode('utf-8'))
    return {"status": resp.status_code, "message": rs}


def find_battery_by_id(id):
    uri = url + f'/{id}'
    resp = requests.get(uri, timeout=10)
    rs = json.loads(resp.content.decode('utf-8'))
    return {"status": resp.status_code, "message": rs}


def find_user_by_rfid(rfid):
    uri = url + "/find-user-by-rfid"
    resp = requests.get(uri, timeout=1000, params={"code": rfid})
    rs = json.loads(resp.content.decode('utf-8'))
    return {"status": resp.status_code, "message": rs}

#connect to harware
def read_infor_slot(**karg):
    rfid = karg['rfid']


if __name__ == "__main__":
    data = find_all_battery()
    print(data)
