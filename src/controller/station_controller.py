import json
import requests


def authentic(rfid: str):
    url = "http://localhost:5000/api/battery/find-user-by-rfid?code=" + rfid
    payload = {}
    response = requests.get("GET", url, data=payload)
    json_data = json.loads(response.content.decode('utf-8'))
    return json_data


class PinInStation:
    def __init__(self, slot, rfid, capacity):
        self.slot = slot
        self.rfid = rfid
        self.capacity = capacity


listPin = []
listPin.append(PinInStation(1, "AATX123", 78.05))
listPin.append(PinInStation(2, "AATX093", 45.99))
listPin.append(PinInStation(3, "ARWX783", 98.22))


def check_battery_capacity(slot: int):
    remain_capacity_info = -1
    for obj in listPin:
        if obj.slot == slot:
            remain_capacity_info = obj.capacity
    return remain_capacity_info


def calculate_money(old_capacity: float, new_capacity: float):
    if new_capacity - old_capacity > 0:
        money = int((new_capacity - old_capacity)*10000)
        return money
    else:
        return -1


def check_money(user_wallet: int, money_needed_to_pay: int):
    return user_wallet > money_needed_to_pay


def get_best_battery(): #return slot
    max_capacity = 0
    for obj in listPin:
        if obj.capacity >= max_capacity:
            max_capacity = obj.capacity
            slot = obj.slot
    return slot



def push_battery(is_bellow_thresshold: bool, is_enough_money: bool):
    if not is_bellow_thresshold:
        pass
    else:
        if not is_enough_money:
            print('tra lai pin cho nguoi dung vi khong du tien')
        else:
            return get_best_battery()
        
