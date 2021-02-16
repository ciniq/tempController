import os
from Sensor import Sensor

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
class AllSensors:
  def __init__(self, locations):
      self.locations = locations

  def getAllData(self):
      values = []
      for location in self.locations :
          sen = Sensor(location)
          values.append(sen.get_value())
      return values