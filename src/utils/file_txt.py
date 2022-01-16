import os
from src.config.config import FileConfig as fc
def _read_file(fp):
    with open(fp, 'r') as f:
        data = f.readline()

    infor = data.split('|')
    return infor

def _get_no_slot(fn):
    if "1" in fn:
        return 1
    if "2" in fn:
        return 2
    if "3" in fn:
        return 3

def read_slot_file():
    rs = []
    prefix = fc.BATTERY_PREFIX
    for root, _, fns in os.walk(prefix):
        for fn in fns:
            slot = _get_no_slot(fn)
            fn = root+"/"+fn
            with open(fn, 'r') as f:
                data = f.readline()
            if len(data)!=0:
                data = str(slot)+"|"+data
            else:
                data = str(slot)+"|"
            rs.append(data)
            
    return rs

def _check_empty_slot():
    prefix = fc.BATTERY_PREFIX
    for root, _, fns in os.walk(prefix):
        for fn in fns:
            fo = fn
            fn = root+'/'+fn
            with open(fn, 'r') as f:
                data = f.readline()
                data = data.split('|')
                if 'X' in data[0]:
                    return fo
                
def write_to_empty_slot(data):
    empty_slot = _check_empty_slot()
    prefix = fc.BATTERY_PREFIX
    fp = prefix+'/'+empty_slot
    with open(fp, 'w') as f:
        f.write(data)
        
def get_info(slot_file):
    fp = fc.BATTERY_PREFIX+'/'+slot_file
    with open(fp, 'r') as f:
        data = f.readline()
    return data

if __name__ == "__main__":
    fn = _check_empty_slot()
    print(fn)
                

            
            
            