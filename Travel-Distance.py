from math import acos, sin, cos, radians, floor
RADIUS_MILES = 3963

class DestinationCalculator:
    def __init__(self):
        self.locations = []
        self.loc_str = []
    
    def process(self, line: str) -> str:
        if line[:3] == 'LOC':
            line_list = line.split(':')
            self.loc_str.append(line_list[1])
            self.locations.append([radians(float(line_list[2])), radians(float(line_list[3]))])
            return(line[4:7])
        else:
            ac_no = line.split(":")[1]
            
            delta = abs(self.locations[0][1] - self.locations[1][1])
            delta_sigma = acos((sin(self.locations[0][0])*sin(self.locations[1][0])) + (cos(self.locations[0][0])*cos(self.locations[1][0])*cos(delta)))
            distance = floor(RADIUS_MILES * delta_sigma)
            
            output = ac_no + ":" + self.loc_str[0] + ":" + self.loc_str[1] + ":" + str(distance)
            
            return(output)