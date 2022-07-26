class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds
class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2
    def __str__(self):
        return f'{len(self)//3600:02d}: {(len(self)%3600)//60:02d}: {(len(self))%60:02d}'        
    def __len__(self):
        return 0 if self.clock1.get_time()<self.clock2.get_time() else self.clock1.get_time()-self.clock2.get_time()
    
