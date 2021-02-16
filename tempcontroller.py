import glob
import classes.AllSensors

sensors = AllSensors(glob.glob('/sys/bus/w1/devices/28*'))

while True:
    print(sensors.getAllData())