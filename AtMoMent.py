import webiopi
import subprocess
import os
from time import sleep

GPIO = webiopi.GPIO

pos_shu = 17 #shutter_button


def setup():
    GPIO.setFunction(pos_shu,GPIO.OUT)

def loop():
    webiopi.sleep(0.5)

    if GPIO.digitalRead(pos_shu)==GPIO.LOW:
        GPIO.digitalWrite(pos_shu, GPIO.HIGH)
        cmd = "raspistill -o ./work/Ltka/moment.jpg -t 1"
        subprocess.call(cmd, shell=True)
        webiopi.sleep(1)
    
#    if GPIO.digitalRead(pos_shu) == GPIO.HIGH:
#        GPIO.digitalWrite(pos_shu, GPIO.LOW)
#        webiopi.sleep(1)
    
def destroy():
    GPIO.digitalWrite(LIGHT, GPIO.LOW)
#def destroy():
#    webiopi.sleep(0.5)
#    GPIO.digitalWrite(pos_shu, GPIO.HIGH)
#    GPIO.digitalWrite(pos_bon, GPIO.HIGH)
