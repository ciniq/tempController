import time

class Sensor:
    
    location = ''
    
    def __init__(self, location):
        self.location = location

    def __get_raw_temp(self):
        f = open(self.location + '/w1_slave', 'r')
        lines = f.readlines()
        f.close()
        return lines
    
    def get_value(self):
        lines = __get_raw_temp(location)
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = __get_raw_temp(location)
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            return float(temp_string) / 1000.0
            
    