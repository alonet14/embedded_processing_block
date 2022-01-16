from src.model.user import User
from src.service.battery_service import find_user_by_rfid

def get_user(rfid):
    data = find_user_by_rfid(rfid)
    return data
    
    
if __name__ == "__main__":
    data = get_user("AAXX564H")
    print(data)