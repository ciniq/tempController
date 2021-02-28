import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
RELAIS_1_GPIO = 25
RELAIS_2_GPIO = 18

relais_1 = True
relais_2 = False

GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode
GPIO.setup(RELAIS_2_GPIO, GPIO.OUT) # GPIO Assign mode
while True :
    sleep(1)
    if (relais_1 == True) :
        print('relais 1 aan')
        relais_1 = False
        GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out
    else :
        print('relais 1 uit')
        relais_1 = True
        GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on
    
    if (relais_2 == True) :
        print('relais 2 aan')
        relais_2 = False
        GPIO.output(RELAIS_2_GPIO, GPIO.LOW) # out
    else :
        print('relais 2 uit')
        relais_2 = True
        GPIO.output(RELAIS_2_GPIO, GPIO.HIGH) # on
    

