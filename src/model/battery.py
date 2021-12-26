
class Battery():
    def __init__(self, rfid, capacity):
        self.rfid = rfid
        assert 0 < capacity <= 100
        self.capacity = capacity

    def increase_capacity(self):
        if self.capacity < 100:
            self.capacity += 1

    def is_over_threshold(self)->bool:
        return self.capacity < 80


