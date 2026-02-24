import datetime

class Booking:
    def __init__(self, email,number, slot):
        self.email = email
        self.number = number
        self.time = datetime.now
        self.slot = slot
        
    def hashfunc(self)-> int:
        return hash(self.email, self.number, self.time, self.slot)
    
    def compare(self, obj) -> bool:
        if(self.email == obj.email and self.number == obj.email and self.slot == obj.slot and self.time == obj.time):
            return True
        return False
        

        

