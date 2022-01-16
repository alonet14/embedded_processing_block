
class Config(object):
    HOST = 'http://103.82.22.26'
    PORT = "5000"

class StationConfig:
    N_SLOT=4
    ID=1

class FileConfig:
    BATTERY_PREFIX = 'D:/project/embedded_processing_block/battery_in'
    
class Command(object):
    CHANGE_INFO_BATTERY=0
    GET_INFO_USER=1
    