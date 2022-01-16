from src.model.battery import Battery
from src.model.slot import Slot
    
class Station:
    def __init__(self, location, list_slot: list()):
        self.location = location
        self.list_slot = list_slot

    def best_battery(self) -> list:
        return [e for e in self.list_battery if e.capacity >= 95]

    
