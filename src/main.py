# Importing Libraries
from queue import Queue
import serial
import time
import src.utils.file_txt as fu
import src.controller.station_controller as sc
arduino = serial.Serial(port = 'COM1',
                        baudrate=9600,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout=0)


#value sent format
#b| : battery info
#u| : user info
#i| : sent battery which is over threshold
#n| : battery's suitable but not enough money
#

def send_data(x):
    
    arduino.write(x)
    arduino.flush()
    time.sleep(0.2)

#buffer
new_data = []
is_newdata = False

def read_data():
    global is_newdata
    global new_data
    data = arduino.read()
    
    if data != b'':
        new_data.append(data)
        new_data = [e for e in new_data if e!=b'\n' and e!=b'\r']
        if data == b'\n':
            if len(new_data) != 0:
                is_newdata = True  
        
def sync_battery_info():
    data = fu.read_slot_file()
    data = [e+'\n' for e in data]
    data = ['b|'+e for e in data]
    for d in data:  
        send_data(d.encode('ascii'))
        print(d.encode('ascii'))
        time.sleep(1)
        
    arduino.break_condition = True
    time.sleep(4)
    arduino.break_condition = False

def check_capacity():
    #convert byte to string
    #data in form 1|AAXX564H|10
    global new_data
    data = [e for e in new_data if e!=b'\x08']
    data = [e.decode('ascii') for e in data]
    data = ''.join(data)
    data = data.split('|')
    if not sc.check_suitable_capacity(int(data[-1])):
        message = f'i|{data[0]}'
        send_data(message.encode('ascii'))
    else:
        slot=sc.get_best_battery()
        info = fu.read_slot_file(slot)
        info = info.split('|')
        info_user = sc.show_info_user(data[1])
        new_capacity = int(info[1])
        old_capacity = int(data[2])
        
        money_to_pay = sc.calculate_money(old_capacity, new_capacity)
        is_enough_money = sc.check_money(info_user['wallet'], money_to_pay)
        if not is_enough_money:
            #n = not enought money
            message = f'n|{data[0]}'
            send_data(message.encode('ascii'))
        else:
            val_battery_in = '|'.join([data[1], data[2]], '0')
            slot_file_name_in = f'slot_{data[0]}.txt'
            sc.push_battery(val_battery_in, slot_file_name_in, slot)
            #sent mess to hardware here
            
            
            
            pass
            
            
        
        
    

arduino.write(b'1')
while True:
    sc.increase_battery_capacity()
    sync_battery_info()
    
   
    read_data()
    time.sleep(0.2)
    
    
    if len(new_data) != 0 and is_newdata:
        print(new_data)
        check_capacity()
       
        new_data = []
        is_newdata = False
