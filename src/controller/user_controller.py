from model.user import User
from service.battery import find_user_by_rfid

def get_user(rfid):
    data = find_user_by_rfid(rfid)
    