#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
from time import sleep
#from subprocess import call
import os
#from subprocess import call
import paho.mqtt.publish as publish

#publish.single("pill/19", "boaaao", hostname="localhost")

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(26, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(19, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(13, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(21, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(16, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(20, GPIO.OUT, initial=GPIO.HIGH)

#Stock
pill26 = 1000
pill19 = 1000
pill13 = 1000
pill21 = 1000
pill16 = 1000
pill20 = 1000

while True: # Run forever
    print("=== Pordee pill v0.1===")
    print("waiting for card")
    sleep(1.5)
    #GPIO.cleanup()
    GPIO.output(26, GPIO.HIGH) #1 100 150
    GPIO.output(19, GPIO.HIGH) #2 200 250
    GPIO.output(13, GPIO.HIGH) #3 300 350
    GPIO.output(21, GPIO.HIGH) #4 400 45
    GPIO.output(16, GPIO.HIGH) #5 500 550
    GPIO.output(20, GPIO.HIGH) #6 600 650

    reader = SimpleMFRC522.SimpleMFRC522()
    id, text = reader.read()
    print(id)
    print(text)

    if id == 649904026617: #Jason
        ###JASON###
        
        #pill19
        GPIO.output(19, GPIO.LOW)
        publish.single("customer/jason/19", 250, hostname="localhost")
        pill19 = pill19 - 1
        print("stock pill 19 = " + pill19)
        publish.single("pill/19", pill19, hostname="localhost")
        
        #pill26
        GPIO.output(26, GPIO.LOW)
        publish.single("customer/jason/26", 150, hostname="localhost")
        pill26 = pill26 - 1
        print("stock pill 26 = " + pill26)
        publish.single("pill/26", pill26, hostname="localhost")
        
        #pill20
        GPIO.output(20, GPIO.LOW)
        publish.single("customer/jason/20", 650, hostname="localhost")
        pill20 = pill20 - 1
        print("stock pill 20 = " + pill20)
        publish.single("pill/20", pill20, hostname="localhost")
        
        #pill21
        GPIO.output(21, GPIO.LOW)
        publish.single("customer/jason/21", 450, hostname="localhost")
        pill21 = pill21 - 1
        print("stock pill 21 = " + pill21)
        publish.single("pill/21", pill21, hostname="localhost")
        
        print("Jason: 19, 26, 20, 21")
        sleep(0.5)
        
        #pill19
        GPIO.output(19, GPIO.HIGH)
        publish.single("customer/jason/19", 200, hostname="localhost")
        
        #pill26
        GPIO.output(26, GPIO.HIGH)
        publish.single("customer/jason/26", 100, hostname="localhost")
        
        #pill20
        GPIO.output(20, GPIO.HIGH)
        publish.single("customer/jason/20", 600, hostname="localhost")
        
        #pill21
        GPIO.output(21, GPIO.HIGH)
        publish.single("customer/jason/21", 400, hostname="localhost")

    elif id == 126128487786: #Edward
        ###Edward###
        
        #pill13
        GPIO.output(13, GPIO.LOW)
        publish.single("customer/edward/13", 350, hostname="localhost")
        pill13 = pill13 - 1
        print("stock pill 13 = " + pill13)
        publish.single("pill/13", pill13, hostname="localhost")
        
        #pill16
        GPIO.output(16, GPIO.LOW)
        publish.single("customer/edward/16", 550, hostname="localhost")
        pill16 = pill16 - 1
        print("stock pill 16 = " + pill16)
        publish.single("pill/16", pill16, hostname="localhost")
        
        print("Edward: 13, 16")
        sleep(0.5)
        
        #pill13
        GPIO.output(13, GPIO.HIGH)
        publish.single("customer/edward/13", 300, hostname="localhost")
        
        #pill16
        GPIO.output(16, GPIO.HIGH)
        publish.single("customer/edward/16", 500, hostname="localhost")
  
    elif id == 000000123456: #Gordon
        ###Gordon###
        
        #pill19
        GPIO.output(19, GPIO.LOW)
        publish.single("customer/gordon/19", 250, hostname="localhost")
        pill19 = pill19 - 1
        print("stock pill 19 = " + pill19)
        publish.single("pill/19", pill19, hostname="localhost")
        
        #pill26
        GPIO.output(26, GPIO.LOW)
        publish.single("customer/gordon/26", 150, hostname="localhost")
        pill26 = pill26 - 1
        print("stock pill 26 = " + pill26)
        publish.single("pill/26", pill26, hostname="localhost")
        
        print("Gordon: 19, 26")
        sleep(0.5)
        
        #pill19
        GPIO.output(19, GPIO.HIGH)
        publish.single("customer/gordon/19", 200, hostname="localhost")
        
        #pill26
        GPIO.output(26, GPIO.LOW)
        publish.single("customer/gordon/26", 150, hostname="localhost")
        

    elif id == 000011123456: #Henry
        ###Henry###
        
        #pill16
        GPIO.output(16, GPIO.LOW)
        publish.single("customer/henry/16", 550, hostname="localhost")
        pill16 = pill16 - 1
        print("stock pill 16 = " + pill16)
        publish.single("pill/16", pill16, hostname="localhost")
        
        #pill26
        GPIO.output(26, GPIO.LOW)
        publish.single("customer/henry/26", 150, hostname="localhost")
        pill26 = pill26 - 1
        print("stock pill 26 = " + pill26)
        publish.single("pill/26", pill26, hostname="localhost")
        
        #pill13
        GPIO.output(13, GPIO.LOW)
        publish.single("customer/henry/13", 350, hostname="localhost")
        pill13 = pill13 - 1
        print("stock pill 13 = " + pill13)
        publish.single("pill/13", pill13, hostname="localhost")
        
        #pill21
        GPIO.output(21, GPIO.LOW)
        publish.single("customer/henry/21", 450, hostname="localhost")
        pill21 = pill21 - 1
        print("stock pill 21 = " + pill21)
        publish.single("pill/21", pill21, hostname="localhost")
        
        print("Henry: 16, 26, 13, 21")
        sleep(0.5)
        
        #pill16
        GPIO.output(16, GPIO.HIGH)
        publish.single("customer/henry/16", 500, hostname="localhost")
        
        #pill26
        GPIO.output(26, GPIO.HIGH)
        publish.single("customer/henry/26", 100, hostname="localhost")
        
        #pill13
        GPIO.output(13, GPIO.HIGH)
        publish.single("customer/henry/13", 300, hostname="localhost")
        
        #pill21
        GPIO.output(21, GPIO.HIGH)
        publish.single("customer/henry/21", 400, hostname="localhost")
        
                    
    else:
        print("no card found")
