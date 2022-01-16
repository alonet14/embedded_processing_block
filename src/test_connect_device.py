# Importing Libraries
import serial
import time
import 
arduino = serial.Serial(port='COM1', baudrate=9600,
                        bytesize=serial.EIGHTBITS,
                        
                        timeout=0)

def send_data(x):
    arduino.write(x)
    arduino.flush()
    time.sleep(0.2)

new_data = []
is_newdata = False

def read_data():
    global is_newdata
    data = arduino.read()
    if data !=b'':
        new_data.append(data)
        is_newdata = True
        
    time.sleep(0.1)
    return data


while True:
    x = "message\n".encode('ascii')
    
    data = send_data(x)
    read_data()
    # r_data = r_data.decode("ascii")
    # data = bytes.fromhex(data)
    # ascii_string = data.decode('ASCII')
    if len(new_data) != 0 and is_newdata:
        print(new_data)
        is_newdata = False
        new_data = []
