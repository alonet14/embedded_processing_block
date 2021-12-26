from model.battery import Battery
def get_info_slot(fp:str):
    with open(fp, 'r') as f:
        line = fp.readline()
        
    infor = line.split("|")
    rfid = line[0]
    capacity = line[1]
    battery = Battery(rfid, capacity)
    return battery
    

    