import glob
from classes.AllSensors import AllSensors

sensors = AllSensors(glob.glob('/sys/bus/w1/devices/28*'))

while True:
    print(sensors.getAllData())