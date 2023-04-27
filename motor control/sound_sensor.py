import time
import grovepi
import numpy as np

# sensor setup 
ss_a0 = 0
ss_a1 = 1
ss_a2 = 2
grovepi.pinMode(ss_a0,"INPUT")
grovepi.pinMode(ss_a1,"INPUT")
grovepi.pinMode(ss_a2,"INPUT")
threshold = 100

# sensor calibration
a0_calibration = []
a1_calibration = []
a2_calibration = []
for i in range(100):
    a0_calibration.append(grovepi.analogRead(ss_a0))
    a1_calibration.append(grovepi.analogRead(ss_a1))
    a2_calibration.append(grovepi.analogRead(ss_a2))

a0_calibration = np.average(a0_calibration)
a1_calibration = np.average(a1_calibration)
a2_calibration = np.average(a2_calibration)


while True:
    try:
        # Read the sound level
        a0_val = grovepi.analogRead(ss_a0) - a0_calibration
        a1_val = grovepi.analogRead(ss_a1) - a1_calibration
        a2_val = grovepi.analogRead(ss_a2) - a2_calibration

        # Print sound sensor values (for debugging)
        print("a0 = %d" %a0_val)
        print("a1 = %d" %a1_val)
        print("a2 = %d" %a2_val)

        # Move according to loudest sensor
        if (a0_val > threshold or a1_val > threshold or a2_val > threshold):
            if (a0_val > a1_val and a0_val > a2_val):
                print("LEFT")
            if (a1_val > a0_val and a1_val > a2_val):
                print("FORWARD")
            if (a2_val > a0_val and a2_val > a1_val):
                print("RIGHT")
                
        time.sleep(1)

 
    except IOError:
        print ("Error")
