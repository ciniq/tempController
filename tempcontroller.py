import glob
import time
from datetime import datetime
from AllSensors import AllSensors

sensors = AllSensors(glob.glob('/sys/bus/w1/devices/28*'))

while True:
    time.sleep(60)
    dt = datetime.now()
    sen = sensors.getAllData()
    print(str(sen[0]) +' - ' + dt.strftime("%d/%m/%Y %H:%M:%S"))