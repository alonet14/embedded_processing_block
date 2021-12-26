from random import randrange
from battery import Battery

class Slot:
    def __init__(self, no, battery: Battery, is_charge_mode):
        self.no = no
        self.battery = battery
        self.is_charge_mode = is_charge_mode
        
    def status(self):
        return self.battery is not None
    
    
class Station:
    def __init__(self, location, list_slot: list()):
        self.location = location
        self.list_slot = list_slot

    def best_battery(self) -> list:
        return [e for e in self.list_battery if e.capacity >= 95]

    
