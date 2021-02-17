import glob
import time
from AllSensors import AllSensors

sensors = AllSensors(glob.glob('/sys/bus/w1/devices/28*'))

while True:
    time.sleep(5)
    print(sensors.getAllData())