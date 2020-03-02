#!/usr/bin/python3

import time
import pyfirmata
board = pyfirmata.ArduinoMega('/dev/ttyACM0')  # arduino setup

# import only system from os 
from os import system, name 

# define our clear function 
def clear(): 

	# for windows 
	if name == 'nt': 
		_ = system('cls') 

	# for mac and linux(here, os.name is 'posix')
	else: 
		_ = system('clear') 


it = pyfirmata.util.Iterator(board)
it.start()

speed = 1
hold=.0050
threshold = 0.05

# define the sliders tuple: This corresponds to the 1-16 labels on the vinophonics front panel

sliders = (1, 5, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)

# declare pin assignments for reading the potentiometer position

time.sleep(1)
slider_1	 = board.get_pin('a:0:i')
slider_2	 = board.get_pin('a:1:i')
slider_3	 = board.get_pin('a:2:i')
slider_4	 = board.get_pin('a:3:i')
slider_5	 = board.get_pin('a:4:i')
slider_6	 = board.get_pin('a:5:i')
slider_7	 = board.get_pin('a:6:i')
slider_8	 = board.get_pin('a:7:i')
slider_9	 = board.get_pin('a:8:i')
slider_10	 = board.get_pin('a:9:i')
slider_11	 = board.get_pin('a:10:i')
slider_12	 = board.get_pin('a:11:i')
slider_13	 = board.get_pin('a:12:i')
slider_14	 = board.get_pin('a:13:i')
slider_15	 = board.get_pin('a:14:i')
slider_16	 = board.get_pin('a:15:i')

# declare pin assignments to control the H-Bridge direction

slider_1_enable	    = board.get_pin('d:13:p')
slider_1_up		    = board.get_pin('d:22:o')
slider_1_down	    = board.get_pin('d:24:o')
slider_2_enable	    = board.get_pin('d:12:p')
slider_2_up		    = board.get_pin('d:32:o')
slider_2_down	    = board.get_pin('d:30:o')
slider_3_enable	    = board.get_pin('d:9:p')
slider_3_up		    = board.get_pin('d:28:o')
slider_3_down	    = board.get_pin('d:26:o')
slider_4_enable	    = board.get_pin('d:8:p')
slider_4_up		    = board.get_pin('d:36:o')
slider_4_down	    = board.get_pin('d:34:o')
slider_5_enable	    = board.get_pin('d:5:p')
slider_5_up		    = board.get_pin('d:40:o')
slider_5_down	    = board.get_pin('d:38:o')
slider_6_enable	    = board.get_pin('d:4:p')
slider_6_up		    = board.get_pin('d:44:o')
slider_6_down	    = board.get_pin('d:42:o')
slider_7_enable	    = board.get_pin('d:14:o')
slider_7_up		    = board.get_pin('d:48:o')
slider_7_down	    = board.get_pin('d:46:o')
slider_8_enable	    = board.get_pin('d:15:o')
slider_8_up		    = board.get_pin('d:52:o')
slider_8_down	    = board.get_pin('d:50:o')
slider_9_enable	    = board.get_pin('d:11:p')
slider_9_up		    = board.get_pin('d:23:o')
slider_9_down	    = board.get_pin('d:25:o')
slider_10_enable	= board.get_pin('d:10:p')
slider_10_up		= board.get_pin('d:27:o')
slider_10_down		= board.get_pin('d:29:o')
slider_11_enable	= board.get_pin('d:6:p')
slider_11_up	    = board.get_pin('d:31:o')
slider_11_down	    = board.get_pin('d:33:o')
slider_12_enable	= board.get_pin('d:7:p')
slider_12_up	    = board.get_pin('d:35:o')
slider_12_down	    = board.get_pin('d:37:o')
slider_13_enable	= board.get_pin('d:3:p')
slider_13_up	    = board.get_pin('d:41:o')
slider_13_down	    = board.get_pin('d:39:o')
slider_14_enable	= board.get_pin('d:2:p')
slider_14_up	    = board.get_pin('d:45:o')
slider_14_down    	= board.get_pin('d:43:o')
slider_15_enable	= board.get_pin('d:16:o')
slider_15_up	    = board.get_pin('d:49:o')
slider_15_down	    = board.get_pin('d:47:o')
slider_16_enable	= board.get_pin('d:17:o')
slider_16_up	    = board.get_pin('d:53:o')
slider_16_down	    = board.get_pin('d:51:o')

slider_1_targetValue = 0.7
slider_2_targetValue = 0.8
slider_3_targetValue = .33
slider_4_targetValue = .5
slider_5_targetValue = .7
slider_6_targetValue = .4
slider_7_targetValue = .9
slider_8_targetValue = .3
slider_9_targetValue = .7
slider_10_targetValue = .3
slider_11_targetValue = .4
slider_12_targetValue = .7
slider_13_targetValue = .4
slider_14_targetValue = .5
slider_15_targetValue = .9
slider_16_targetValue = .9

slider_1_pos = (slider_1.read())
slider_2_pos = (slider_2.read())
slider_3_pos = (slider_3.read())
slider_4_pos = (slider_4.read())
slider_5_pos = (slider_5.read())
slider_6_pos = (slider_6.read())
slider_7_pos = (slider_7.read())
slider_8_pos = (slider_8.read())
slider_9_pos = (slider_9.read())
slider_10_pos = (slider_10.read())
slider_11_pos = (slider_11.read())
slider_12_pos = (slider_12.read())
slider_13_pos = (slider_13.read())
slider_14_pos = (slider_14.read())
slider_15_pos = (slider_15.read())
slider_16_pos = (slider_16.read())

time.sleep(1)

slider_1_pos = (slider_1.read())
slider_2_pos = (slider_2.read())
slider_3_pos = (slider_3.read())
slider_4_pos = (slider_4.read())
slider_5_pos = (slider_5.read())
slider_6_pos = (slider_6.read())
slider_7_pos = (slider_7.read())
slider_8_pos = (slider_8.read())
slider_9_pos = (slider_9.read())
slider_10_pos = (slider_10.read())
slider_11_pos = (slider_11.read())
slider_12_pos = (slider_12.read())
slider_13_pos = (slider_13.read())
slider_14_pos = (slider_14.read())
slider_15_pos = (slider_15.read())
slider_16_pos = (slider_16.read())

while True:
        slider_1_pos = float(slider_1.read())
        slider_2_pos = float(slider_2.read())
        slider_3_pos = float(slider_3.read())
        slider_4_pos = float(slider_4.read())
        slider_5_pos = float(slider_5.read())
        slider_6_pos = float(slider_6.read())
        slider_7_pos = float(slider_7.read())
        slider_8_pos = float(slider_8.read())
        slider_9_pos = float(slider_9.read())
        slider_10_pos = float(slider_10.read())
        slider_11_pos = float(slider_11.read())
        slider_12_pos = float(slider_12.read())
        slider_13_pos = float(slider_13.read())
        slider_14_pos = float(slider_14.read())
        slider_15_pos = float(slider_15.read())
        slider_16_pos = float(slider_16.read())
        print("Slider 1: ", slider_1_pos)
        print("Slider 2: ", slider_2_pos)
        print("Slider 3: ", slider_3_pos)
        print("Slider 4: ", slider_4_pos)
        print("Slider 5: ", slider_5_pos)
        print("Slider 6: ", slider_6_pos)
        print("Slider 7: ", slider_7_pos)
        print("Slider 8: ", slider_8_pos)
        print("Slider 9: ", slider_9_pos)
        print("Slider 10: ", slider_10_pos)
        print("Slider 11: ", slider_11_pos)
        print("Slider 12: ", slider_12_pos)
        print("Slider 13: ", slider_13_pos)
        print("Slider 14: ", slider_14_pos)
        print("Slider 15: ", slider_15_pos)
        print("Slider 16: ", slider_16_pos)

#       time.sleep(.01)
        if (slider_1_pos - slider_1_targetValue) > threshold and (slider_1_pos > slider_1_targetValue):
            slider_1_up.write(0)
            slider_1_down.write(1)
            slider_1_enable.write(1)
            time.sleep(hold)
            slider_1_enable.write(0)
            slider_1_pos = float(slider_1.read())
        elif (slider_1_targetValue - slider_1_pos) > threshold and (slider_1_pos < slider_1_targetValue):
            slider_1_up.write(1)
            slider_1_down.write(0)
            slider_1_enable.write(1)
            time.sleep(hold)
            slider_1_enable.write(0)
            slider_1_pos = float(slider_1.read())
        else:
            slider_1_enable.write(0)

        if (slider_2_pos - slider_2_targetValue) > threshold and (slider_2_pos > slider_2_targetValue):
            slider_2_up.write(0)
            slider_2_down.write(1)
            slider_2_enable.write(speed)
            time.sleep(hold)
            slider_2_enable.write(0)
            slider_2_pos = float(slider_2.read())
        elif (slider_2_targetValue - slider_2_pos) > threshold and (slider_2_pos < slider_2_targetValue):
            slider_2_up.write(1)
            slider_2_down.write(0)
            slider_2_enable.write(speed)
            time.sleep(hold)
            slider_2_enable.write(0)
            slider_2_pos = float(slider_2.read())
        else:
            slider_2_enable.write(0)

        if (slider_3_pos - slider_3_targetValue) > threshold and (slider_3_pos > slider_3_targetValue):
            slider_3_up.write(0)
            slider_3_down.write(1)
            slider_3_enable.write(speed)
            time.sleep(hold)
            slider_3_enable.write(0)
            slider_3_pos = float(slider_3.read())
        elif (slider_3_targetValue - slider_3_pos) > threshold and (slider_3_pos < slider_3_targetValue):
            slider_3_up.write(1)
            slider_3_down.write(0)
            slider_3_enable.write(speed)
            time.sleep(hold)
            slider_3_enable.write(0)
            slider_3_pos = float(slider_3.read())
        else:
            slider_3_enable.write(0)

        if (slider_4_pos - slider_4_targetValue) > threshold and (slider_4_pos > slider_4_targetValue):
            slider_4_up.write(0)
            slider_4_down.write(1)
            slider_4_enable.write(speed)
            time.sleep(hold)
            slider_4_enable.write(0)
            slider_4_pos = float(slider_4.read())
        elif (slider_4_targetValue - slider_4_pos) > threshold and (slider_4_pos < slider_4_targetValue):
            slider_4_up.write(1)
            slider_4_down.write(0)
            slider_4_enable.write(speed)
            time.sleep(hold)
            slider_4_enable.write(0)
            slider_4_pos = float(slider_4.read())
        else:
            slider_4_enable.write(0)

        if (slider_5_pos - slider_5_targetValue) > threshold and (slider_5_pos > slider_5_targetValue):
            slider_5_up.write(0)
            slider_5_down.write(1)
            slider_5_enable.write(speed)
            time.sleep(hold)
            slider_5_enable.write(0)
            slider_5_pos = float(slider_5.read())
        elif (slider_5_targetValue - slider_5_pos) > threshold and (slider_5_pos < slider_5_targetValue):
            slider_5_up.write(1)
            slider_5_down.write(0)
            slider_5_enable.write(speed)
            time.sleep(hold)
            slider_5_enable.write(0)
            slider_5_pos = float(slider_5.read())
        else:
            slider_5_enable.write(0)

        if (slider_6_pos - slider_6_targetValue) > threshold and (slider_6_pos > slider_6_targetValue):
            slider_6_up.write(0)
            slider_6_down.write(1)
            slider_6_enable.write(speed)
            time.sleep(hold)
            slider_6_enable.write(0)
            slider_6_pos = float(slider_6.read())
        elif (slider_6_targetValue - slider_6_pos) > threshold and (slider_6_pos < slider_6_targetValue):
            slider_6_up.write(1)
            slider_6_down.write(0)
            slider_6_enable.write(speed)
            time.sleep(hold)
            slider_6_enable.write(0)
            slider_6_pos = float(slider_6.read())
        else:
            slider_6_enable.write(0)

        if (slider_7_pos - slider_7_targetValue) > threshold and (slider_7_pos > slider_7_targetValue):
            slider_7_up.write(0)
            slider_7_down.write(1)
            slider_7_enable.write(speed)
            time.sleep(hold)
            slider_7_enable.write(0)
            slider_7_pos = float(slider_7.read())
        elif (slider_7_targetValue - slider_7_pos) > threshold and (slider_7_pos < slider_7_targetValue):
            slider_7_up.write(1)
            slider_7_down.write(0)
            slider_7_enable.write(speed)
            time.sleep(hold)
            slider_7_enable.write(0)
            slider_7_pos = float(slider_7.read())
        else:
            slider_7_enable.write(0)

        if (slider_8_pos - slider_8_targetValue) > threshold and (slider_8_pos > slider_8_targetValue):
            slider_8_up.write(0)
            slider_8_down.write(1)
            slider_8_enable.write(speed)
            time.sleep(hold)
            slider_8_enable.write(0)
            slider_8_pos = float(slider_8.read())
        elif (slider_8_targetValue - slider_8_pos) > threshold and (slider_8_pos < slider_8_targetValue):
            slider_8_up.write(1)
            slider_8_down.write(0)
            slider_8_enable.write(speed)
            time.sleep(hold)
            slider_8_enable.write(0)
            slider_8_pos = float(slider_8.read())
        else:
            slider_8_enable.write(0)

        if (slider_9_pos - slider_9_targetValue) > threshold and (slider_9_pos > slider_9_targetValue):
            slider_9_up.write(0)
            slider_9_down.write(1)
            slider_9_enable.write(speed)
            time.sleep(hold)
            slider_9_enable.write(0)
            slider_9_pos = float(slider_9.read())
        elif (slider_9_targetValue - slider_9_pos) > threshold and (slider_9_pos < slider_9_targetValue):
            slider_9_up.write(1)
            slider_9_down.write(0)
            slider_9_enable.write(speed)
            time.sleep(hold)
            slider_9_enable.write(0)
            slider_9_pos = float(slider_9.read())
        else:
            slider_9_enable.write(0)

        if (slider_10_pos - slider_10_targetValue) > threshold and (slider_10_pos > slider_10_targetValue):
            slider_10_up.write(0)
            slider_10_down.write(1)
            slider_10_enable.write(speed)
            time.sleep(hold)
            slider_10_enable.write(0)
            slider_10_pos = float(slider_10.read())
        elif (slider_10_targetValue - slider_10_pos) > threshold and (slider_10_pos < slider_10_targetValue):
            slider_10_up.write(1)
            slider_10_down.write(0)
            slider_10_enable.write(speed)
            time.sleep(hold)
            slider_10_enable.write(0)
            slider_10_pos = float(slider_10.read())
        else:
            slider_10_enable.write(0)

        if (slider_11_pos - slider_11_targetValue) > threshold and (slider_11_pos > slider_11_targetValue):
            slider_11_up.write(0)
            slider_11_down.write(1)
            slider_11_enable.write(speed)
            time.sleep(hold)
            slider_11_enable.write(0)
            slider_11_pos = float(slider_11.read())
        elif (slider_11_targetValue - slider_11_pos) > threshold and (slider_11_pos < slider_11_targetValue):
            slider_11_up.write(1)
            slider_11_down.write(0)
            slider_11_enable.write(speed)
            time.sleep(hold)
            slider_11_enable.write(0)
            slider_11_pos = float(slider_11.read())
        else:
            slider_11_enable.write(0)

        if (slider_12_pos - slider_12_targetValue) > threshold and (slider_12_pos > slider_12_targetValue):
            slider_12_up.write(0)
            slider_12_down.write(1)
            slider_12_enable.write(speed)
            time.sleep(hold)
            slider_12_enable.write(0)
            slider_12_pos = float(slider_12.read())
        elif (slider_12_targetValue - slider_12_pos) > threshold and (slider_12_pos < slider_12_targetValue):
            slider_12_up.write(1)
            slider_12_down.write(0)
            slider_12_enable.write(speed)
            time.sleep(hold)
            slider_12_enable.write(0)
            slider_12_pos = float(slider_12.read())
        else:
            slider_12_enable.write(0)

        if (slider_13_pos - slider_13_targetValue) > threshold and (slider_13_pos > slider_13_targetValue):
            slider_13_up.write(0)
            slider_13_down.write(1)
            slider_13_enable.write(speed)
            time.sleep(hold)
            slider_13_enable.write(0)
            slider_13_pos = float(slider_13.read())
        elif (slider_13_targetValue - slider_13_pos) > threshold and (slider_13_pos < slider_13_targetValue):
            slider_13_up.write(1)
            slider_13_down.write(0)
            slider_13_enable.write(speed)
            time.sleep(hold)
            slider_13_enable.write(0)
            slider_13_pos = float(slider_13.read())
        else:
            slider_13_enable.write(0)

        if (slider_14_pos - slider_14_targetValue) > threshold and (slider_14_pos > slider_14_targetValue):
            slider_14_up.write(0)
            slider_14_down.write(1)
            slider_14_enable.write(speed)
            time.sleep(hold)
            slider_14_enable.write(0)
            slider_14_pos = float(slider_14.read())
        elif (slider_14_targetValue - slider_14_pos) > threshold and (slider_14_pos < slider_14_targetValue):
            slider_14_up.write(1)
            slider_14_down.write(0)
            slider_14_enable.write(speed)
            time.sleep(hold)
            slider_14_enable.write(0)
            slider_14_pos = float(slider_14.read())
        else:
            slider_14_enable.write(0)

        if (slider_15_pos - slider_15_targetValue) > threshold and (slider_15_pos > slider_15_targetValue):
            slider_15_up.write(0)
            slider_15_down.write(1)
            slider_15_enable.write(speed)
            time.sleep(hold)
            slider_15_enable.write(0)
            slider_15_pos = float(slider_15.read())
        elif (slider_15_targetValue - slider_15_pos) > threshold and (slider_15_pos < slider_15_targetValue):
            slider_15_up.write(1)
            slider_15_down.write(0)
            slider_15_enable.write(speed)
            time.sleep(hold)
            slider_15_enable.write(0)
            slider_15_pos = float(slider_15.read())
        else:
            slider_15_enable.write(0)

        if (slider_16_pos - slider_16_targetValue) > threshold and (slider_16_pos > slider_16_targetValue):
            slider_16_up.write(0)
            slider_16_down.write(1)
            slider_16_enable.write(speed)
            time.sleep(hold)
            slider_16_enable.write(0)
            slider_16_pos = float(slider_16.read())
        elif (slider_16_targetValue - slider_16_pos) > threshold and (slider_16_pos < slider_16_targetValue):
            slider_16_up.write(1)
            slider_16_down.write(0)
            slider_16_enable.write(speed)
            time.sleep(hold)
            slider_16_enable.write(0)
            slider_16_pos = float(slider_16.read())
        else:
            slider_16_enable.write(0)

#print("Slider 1 position: ")
#print(slider_1_pos)
#print("Slider 1 target value: ")
#print(slider_1_targetValue)
#print("Slider threshold: ")
#print(threshold)
#slider_1_enable.write(0)


clear()
board.exit()

