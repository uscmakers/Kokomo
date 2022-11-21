import time
import grovepi

# sensor setup 
ss_a0 = 0
ss_a1 = 1
ss_a2 = 2
grovepi.pinMode(ss_a0,"INPUT")
grovepi.pinMode(ss_a1,"INPUT")
grovepi.pinMode(ss_a2,"INPUT")

threshold = 400
 
while True:
    try:
        # Read the sound level
        a0_val = grovepi.analogRead(ss_a0)
        a1_val = grovepi.analogRead(ss_a1)
        a2_val = grovepi.analogRead(ss_a2)

        # Print sound sensor values (for debugging)
        print("a0 = %d" %a0_val)
        print("a1 = %d" %a1_val)
        print("a2 = %d" %a2_val)

        # Move according to loudest sensor
        if (a0_val > threshold or a0_val > threshold or a0_val > threshold):
            if (a0_val > a1_val and a0_val > a2_val):
                print("LEFT")
            if (a1_val > a0_val and a1_val > a2_val):
                print("FORWARD")
            if (a2_val > a0_val and a2_val > a1_val):
                print("RIGHT")

 
    except IOError:
        print ("Error")
