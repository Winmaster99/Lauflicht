#Lauflicht mit 10 LEDs
#Hardware / Schaltplan
#Winmaster99 Version 0.01 12.10.2021


from machine import Pin
import time


#Pinbelegung
led1 = Pin(2,Pin.OUT)
led2 = Pin(27,Pin.OUT)
led3 = Pin(26,Pin.OUT)
led4 = Pin(25,Pin.OUT)
led5 = Pin(33,Pin.OUT)
led6 = Pin(32,Pin.OUT)
led7 = Pin(13,Pin.OUT)
led8 = Pin(17,Pin.OUT)
led9 = Pin(12,Pin.OUT)
led10 = Pin(15,Pin.OUT)

#Lauflicht Schleife
while True:
    time.sleep(0.1)
    led1.value(1)
    time.sleep(0.1)
    led2.value(1)
    time.sleep(0.1)
    led3.value(1)
    time.sleep(0.1)
    led4.value(1)
    time.sleep(0.1)
    led5.value(1)
    time.sleep(0.1)
    led6.value(1)
    time.sleep(0.1)
    led7.value(1)
    time.sleep(0.1)
    led8.value(1)
    time.sleep(0.1)
    led9.value(1)
    time.sleep(0.1)
    led10.value(1)
    time.sleep(0.1)
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    led5.value(0)
    led6.value(0)
    led7.value(0)
    led8.value(0)
    led9.value(0)
    led10.value(0)
