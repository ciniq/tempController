import os
from classes.Sensor import Sensor

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
class AllSensors:
  def __init__(self, locations):
      self.locations = locations

  def getAllData(self):
      values = [];
      for location in self.locations :
          sensor = Sensor(location)
          values.append(sensor.get_value())
      return values