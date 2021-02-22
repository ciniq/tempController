import glob
import time
from datetime import datetime
from AllSensors import AllSensors

sensors = AllSensors(glob.glob('/sys/bus/w1/devices/28*'))

while True:
    time.sleep(1)
    dt = datetime.now()
    for sen in sensors.getAllData() :
        print(str(sen) +' - ' + dt.strftime("%d/%m/%Y %H:%M:%S"))