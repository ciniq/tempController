import glob
import allsensors

sensors = allsensors(glob.glob('/sys/bus/w1/devices/28*'))

while True:
    print(sensors.getAllData())