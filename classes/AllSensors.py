import os
from classes.sensor import Sensor

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

def __init__(self, locations):
    self.locations = locations

def getAllData(self):
    values = [];
    for location in self.locations :
        sensor = Sensor(location)
        values.append(sensor.get_value())
    return values