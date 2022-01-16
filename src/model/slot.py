from typing import Any
from src.model.battery import Battery
class Slot:
    def __init__(self, no, battery: Any, is_charge_mode:bool):
        self.no = no
        self.battery = battery
        self.is_charge_mode = is_charge_mode
        
    def is_available(self):
        return self.battery is not None
    
    
    