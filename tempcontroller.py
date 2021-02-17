import glob
import time
from datetime import datetime
from AllSensors import AllSensors

sensors = AllSensors(glob.glob('/sys/bus/w1/devices/28*'))

while True:
    time.sleep(5)
    dt = datetime.now()
    print(sensors.getAllData() +' - ' + dt.strftime("%d/%m/%Y %H:%M:%S"))