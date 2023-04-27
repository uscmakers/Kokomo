import RPi.GPIO as GPIO          
from time import sleep

def motor_init()

    in1R = 27
    in2R = 17
    enR = 22

    in1L = 24
    in2L = 23
    enL = 25

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(in1L,GPIO.OUT)
    GPIO.setup(in2L,GPIO.OUT)
    GPIO.setup(enL,GPIO.OUT)
    GPIO.setup(in1R,GPIO.OUT)
    GPIO.setup(in2R,GPIO.OUT)
    GPIO.setup(enR,GPIO.OUT)

    GPIO.output(in1L,GPIO.LOW)
    GPIO.output(in2L,GPIO.LOW)
    GPIO.output(in1R,GPIO.LOW)
    GPIO.output(in2R,GPIO.LOW)

    pL=GPIO.PWM(enL,1000)
    pR=GPIO.PWM(enR,1000)

    pL.start(25)
    pR.start(25)

def motor_start()
    pL.ChangeDutyCycle(50)
    pL.ChangeDutyCycle(50)

def motor_stop()
    pL.ChangeDutyCycle(0)
    pL.ChangeDutyCycle(0)
    
def motor_forward()
    #left forward
    GPIO.output(in1L,GPIO.HIGH)
    GPIO.output(in2L,GPIO.LOW)
    #right forward
    GPIO.output(in1R,GPIO.HIGH)
    GPIO.output(in2R,GPIO.LOW)

def motor_right()
    #left forward
    GPIO.output(in1L,GPIO.HIGH)
    GPIO.output(in2L,GPIO.LOW)
    #right backward
    GPIO.output(in1R,GPIO.LOW)
    GPIO.output(in2R,GPIO.HIGH)

def motor_left()
    #left backward
    GPIO.output(in1L,GPIO.LOW)
    GPIO.output(in2L,GPIO.HIGH)
    #right forward
    GPIO.output(in1R,GPIO.HIGH)
    GPIO.output(in2R,GPIO.LOW)

