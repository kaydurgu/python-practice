
import math

class Track:
    def __init__(self, start_x , start_y):
        self.road = [TrackLine(start_x, start_y, 0)]
    
    def add_track(self, tr):
        self.road.append(tr)

    def get_tracks(self):
        return tuple(self.road)
    def __len__(self):
        ans = 0
        for i in range(1, len(self.road)):
            ans+= math.sqrt((self.road[i].to_x - self.road[i - 1].to_x) ** 2 + (self.road[i].to_y - self.road[i - 1].to_y) ** 2 )
        return int(ans) 
    def __eq__(self, other: object) -> bool:
        return len(self) == len(other)
    def __ne__(self, other: object) -> bool:
        return len(self) != len(other)
    def __gt__(self, other : object) -> bool:
        return len(self) > len(other)
    def __lt__(self, other : object) -> bool:
        return len(self) < len(other)

class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed
        
track1, track2 = Track(0, 0), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2
