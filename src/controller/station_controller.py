import json
# import requests
from src.model.station import Station
import src.service.station_service as ss
import src.controller.user_controller as uc
from src.config.config import StationConfig
from src.utils import file_txt as ft
from src.config.config import FileConfig as fc
import os
import time
import random

_prefix = fc.BATTERY_PREFIX
def check_suitable_capacity(capacity:int):
    return capacity>90

def calculate_money(old_capacity: float, new_capacity: float):
    if new_capacity - old_capacity > 0:
        money = int((new_capacity - old_capacity)*1000)
        return money
    return -1


def check_money(user_wallet: int, money_needed_to_pay: int):
    return user_wallet > money_needed_to_pay


def get_best_battery(): #return slot
    data_battery= []
    for root, _, fns in os.walk(_prefix):
        for fn in fns:
            fp = root+'/'+fn
            with open(fp, 'r') as f:
                data = f.readline()
            if not data.startswith('X'):
                data=data.split('|')
                dtbe = {"slot": fn, "capacity": int(data[1])}
                data_battery.append(dtbe)
    
    if data_battery[0]['capacity'] == data_battery[1]['capacity']:
        cslot = random.randint(0, 1)
        return data_battery[cslot]['slot']
    if data_battery[0]['capacity'] > data_battery[1]['capacity']:
        return data_battery[0]['slot']
    else:
        return data_battery[1]['slot']
            
def push_battery(data_in, slot_file_name_in, slot_file_name_out):
    fbpi = _prefix+'/'+slot_file_name_in
    fbpo = _prefix+'/'+slot_file_name_out    
    with open(fbpi, 'w') as fi:
        fi.write(data_in)
    
    new_val = 'X|00|0'
    with open(fbpo, 'w') as fo:
        fo.write(new_val)

def chage_state_charge(slot_file_name):
    fp =_prefix+'/'+slot_file_name
    with open(fp, 'r') as f:
        data = f.readline()
        
    data = data.split('|')
    rfid = data[0]
    capacity = data[1]
    charge_state = data[2]
    new_charge_state = '1' if charge_state == '0' else '0'
    new_val = '|'.join([rfid, capacity, new_charge_state])
    with open(fp, 'w') as fw:
        fw.write(new_val)
    
def change_user_info_to_db(data):
    pass

def chage_battery_info_to_db(data):
    pass

def get_id_battery_with_rfid(rfid):
    id = 2
    return id

def increase_battery_capacity():
    for root, _, fns in os.walk(_prefix):
        for fn in fns:
            fp = root+'/'+fn
            with open(fp, 'r') as f:
                data = f.readline()
            data = data.split('|')
            if data[0]=='X':
                continue
            rfid = data[0]
            capacity = int(data[1])
            is_charged = data[2]
            
            if capacity < 99 and is_charged == '1':
                capacity+=1
                time.sleep(0.3)
            
            if capacity == 99:
                is_charged = '0'
            
            data = "|".join([rfid, str(capacity),is_charged])
            with open(fp, 'w') as f1:
                f1.write(data)
    
def show_info_user(rfid):
    ui = uc.get_user(rfid)
    name = ui['message']['user']['name']
    money = ui['message']['user']['wallet']
    return {'name':name, 'wallet': int(money)}



if __name__ == "__main__":
    slot = get_best_battery()
    print(slot)
    