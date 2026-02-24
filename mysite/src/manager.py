import datetime

class Booking:
    def __init__(self, email, time, registered_time, number, slot):
        self.email = email
        self.number = number
        self.time = time
        self.slot = slot
        self.registered_time = registered_time
    
    def expiringReservation(self):
        if self.time + datetime.timedelta(days=365) < datetime.datetime.now():
            # call delete reservation
            #checkfunc.delete("from db WHERE name = $1 ")
            #make db call
            return
        else:
            return
        
    def __hash__(self)-> int:
        return hash(self.email, self.number, self.time, self.slot, self.registered_time)
    
    def __eq__(self, obj) -> bool:
        if(self.email == obj.email and self.number == obj.email and self.slot == obj.slot and self.time == obj.time and self.registered_time == obj.registered_time):
            return True
        return False
    

    
        

        

