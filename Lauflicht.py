#Lauflicht mit 10 LEDs
#Hardware / Schaltplan
#Winmaster99 Version 0.01 12.10.2021


from machine import Pin
import time
#Pin_Liste

leds = [2,27,26,25,33,32,13,17,12,15]
for i in range(0,10):
    leds[i] = Pin(leds[i],Pin.OUT)

while True:
    for i in range(0,10):
        leds[i].value(1)
        time.sleep(0.015)
    for i in range(0,10):
        leds[i].value(0)
        time.sleep(0.015) 

