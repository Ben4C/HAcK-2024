
from connections import connect_mqtt, connect_internet
from time import sleep
from constants import WIFI_SSID, WIFI_PASSWORD, MQTT_SERVER, MQTT_USER, MQTT_PASS
from machine import Pin, PWM
from controller import Controller
from motor import FullStepMotor
from microservo import Servo
from ultrasonic import Ultrasonic
import dht
import time

#All pins to the motor controls
#Back Wheels
p1 = Pin(1, Pin.OUT) #Motor 1
p2 = Pin(2, Pin.OUT)
p3 = Pin(3, Pin.OUT) #Motor 2
p4 = Pin(4, Pin.OUT)

#Front Wheels
p5 = Pin(17, Pin.OUT) #Motor 3
p6 = Pin(18, Pin.OUT)
p7 = Pin(19, Pin.OUT) #Motor 4
p8 = Pin(20, Pin.OUT)

#For microcontroller to enable or disable motors
en1 = Pin(0, Pin.OUT)   #Motor 1
en2 = Pin(5, Pin.OUT)   #Motor 2
en3 = Pin(16, Pin.OUT)  #Motor 3
en4 = Pin(21, Pin.OUT)  #Motor 4

#For the stepper pins
s1 = 6
s2 = 7
s3 = 8
s4 = 9

con1 = Controller(p1, p2, p3, p4, en1, en2) #controls back wheels
con2 = Controller(p5, p6, p7, p8, en3, en4) #controls front wheels

en1(1) #enable motor 1
en2(1) #enable motor 2
en3(1) #enable motor 3
en4(1) #enable motor 4

step1 = FullStepMotor.frompins(s1, s2, s3, s4) #stepper controller

micsrv1 = Servo(10) #microservo

#Sensors
ult1 = Ultrasonic(28,27)
humtem = dht.DHT11(Pin(15, Pin.OUT, Pin.PULL_DOWN))

# Function to handle an incoming message

def cb(topic, msg):
#     print(f"Topic: {topic}, Message: {msg}")
    if topic == b"mytopic":
        if msg == b"message":
            print("Ready to Drive!")

    if topic == b"direction": # Drive Train Controls
        if msg == b"forward":
            print("moving forward")
            con1.forward()
            con2.forward()
        if msg == b"stop":
            print("stopping")
            con1.stop()
            con2.stop()
        if msg == b"backward":
            print("moving backward")
            con1.backward()
            con2.backward()
        if msg == b"left":
            print("turning left")
            con1.left()
            con2.right()
        if msg == b"right":
            print("turning right")
            con1.right()
            con2.left()

    if topic == b"arm": # Arm Controls
        print(f"Received message for arm: {msg}")
        if msg == b"right":
            print("Arm going up")
            step1.step(50)
        if msg == b"left":
            print("Arm going down")
            step1.step(-50)
    
    if topic == b"pinch": # Claw Controls
        if msg == b"cw":
            print("pinching claw")
            micsrv1.move(0)
        if msg == b"ccw":
            print("unpinching claw")
            micsrv1.move(60)


def main():
    try:
        connect_internet(WIFI_SSID,WIFI_PASSWORD) #Login to WiFi
        client = connect_mqtt(MQTT_SERVER, MQTT_USER, MQTT_PASS) #Connect to the MQTT Broker
    
        #Subscriptions for MQTT
        client.set_callback(cb)
        client.subscribe("mytopic")
        client.subscribe("direction")
        client.subscribe("arm")
        client.subscribe("pinch")
        client.publish("mytopic", "message")
        
        sleepCount = 0 # Increment used to limit the number of measurements taken and published

        while True:
            client.check_msg()

            sleep(0.01)
            if (sleepCount == 50): # If 50 loops haven't been reached, continue without sensor readings
                sleepCount = 0
                client.publish("ultrasonic", str(ult1.ultra()))
                client.publish("humidity", str(humtem.temperature()))
                client.publish("temp", str(humtem.humidity()))
            else:
                sleepCount += 1 # Increment the sleepcount

    except KeyboardInterrupt:
        print('keyboard interrupt')
        
        
if __name__ == "__main__":
    main()
