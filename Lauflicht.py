#Lauflicht mit 10 LEDs
#Hardware / Schaltplan
#Winmaster99 Version 0.01 12.10.2021


from machine import Pin
from time import sleep

led1 = Pin(2,Pin.OUT)

led1.value(1)
