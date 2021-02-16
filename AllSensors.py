import os
import Sensor

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
class allsensors:
  def __init__(self, locations):
      self.locations = locations

  def getAllData(self):
      values = [];
      for location in self.locations :
          sen = new Sensor(location)
          values.append(sen.get_value())
      return values