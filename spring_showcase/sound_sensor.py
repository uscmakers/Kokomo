import time
import grovepi
import numpy as np

import motor_driver


class SoundSensor:
    def __init__(self):
        # sensor setup 
        self.ss_a0 = 0
        self.ss_a1 = 1
        self.ss_a2 = 2
        grovepi.pinMode(self.ss_a0,"INPUT")
        grovepi.pinMode(self.ss_a1,"INPUT")
        grovepi.pinMode(self.ss_a2,"INPUT")
        self.threshold = 100

        # sensor calibration
        self.a0_calibration = []
        self.a1_calibration = []
        self.a2_calibration = []
        for i in range(100):
            self.a0_calibration.append(grovepi.analogRead(self.ss_a0))
            self.a1_calibration.append(grovepi.analogRead(self.ss_a1))
            self.a2_calibration.append(grovepi.analogRead(self.ss_a2))

        self.a0_calibration = np.average(self.a0_calibration)
        self.a1_calibration = np.average(self.a1_calibration)
        self.a2_calibration = np.average(self.a2_calibration)

        motor_driver.motor_init()

    def run(self):
        motor_driver.motor_start()

        while True:
            try:
                # Read the sound level
                a0_val = grovepi.analogRead(self.ss_a0) - self.a0_calibration
                a1_val = grovepi.analogRead(self.ss_a1) - self.a1_calibration
                a2_val = grovepi.analogRead(self.ss_a2) - self.a2_calibration

                # Print sound sensor values (for debugging)
                print("a0 = %d" %a0_val)
                print("a1 = %d" %a1_val)
                print("a2 = %d" %a2_val)

                # Move according to loudest sensor
                if (a0_val > self.threshold or a1_val > self.threshold or a2_val > self.threshold):
                    if (a0_val > a1_val and a0_val > a2_val):
                        print("LEFT")
                        motor_driver.motor_left()
                    if (a1_val > a0_val and a1_val > a2_val):
                        print("FORWARD")
                        motor_driver.motor_forward()
                    if (a2_val > a0_val and a2_val > a1_val):
                        print("RIGHT")
                        motor_driver.motor_right()
                        
                time.sleep(1)

        
            except IOError:
                print ("Error")
