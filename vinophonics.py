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
hold=10
threshold = 0.15


# declare pin assignments for reading the potentiometer position

slider_one	 = board.get_pin('a:0:i')
slider_two	 = board.get_pin('a:1:i')
slider_three	 = board.get_pin('a:2:i')
slider_four	 = board.get_pin('a:3:i')
slider_five	 = board.get_pin('a:4:i')
slider_six	 = board.get_pin('a:5:i')
slider_seven	 = board.get_pin('a:6:i')
slider_eight	 = board.get_pin('a:7:i')
slider_nine	 = board.get_pin('a:8:i')
slider_ten	 = board.get_pin('a:9:i')
slider_eleven	 = board.get_pin('a:10:i')
slider_twelve	 = board.get_pin('a:11:i')
slider_thirteen	 = board.get_pin('a:12:i')
slider_fourteen	 = board.get_pin('a:13:i')
slider_fifteen	 = board.get_pin('a:14:i')
slider_sixteen	 = board.get_pin('a:15:i')

# declare pin assignments to control the H-Bridge direction

slider_one_enable	= board.get_pin('d:13:p')
slider_one_up		= board.get_pin('d:22:o')
slider_one_down		= board.get_pin('d:24:o')
slider_two_enable	= board.get_pin('d:12:p')
slider_two_up		= board.get_pin('d:32:o')
slider_two_down		= board.get_pin('d:30:o')
slider_three_enable	= board.get_pin('d:9:p')
slider_three_up		= board.get_pin('d:28:o')
slider_three_down	= board.get_pin('d:26:o')
slider_four_enable	= board.get_pin('d:8:p')
slider_four_up		= board.get_pin('d:36:o')
slider_four_down	= board.get_pin('d:34:o')
slider_five_enable	= board.get_pin('d:5:p')
slider_five_up		= board.get_pin('d:40:o')
slider_five_down	= board.get_pin('d:38:o')
slider_six_enable	= board.get_pin('d:4:p')
slider_six_up		= board.get_pin('d:44:o')
slider_six_down		= board.get_pin('d:42:o')
slider_seven_enable	= board.get_pin('d:14:o')
slider_seven_up		= board.get_pin('d:48:o')
slider_seven_down	= board.get_pin('d:46:o')
slider_eight_enable	= board.get_pin('d:15:o')
slider_eight_up		= board.get_pin('d:52:o')
slider_eight_down	= board.get_pin('d:50:o')
slider_nine_enable	= board.get_pin('d:11:p')
slider_nine_up		= board.get_pin('d:23:o')
slider_nine_down	= board.get_pin('d:25:o')
slider_ten_enable	= board.get_pin('d:10:p')
slider_ten_up		= board.get_pin('d:27:o')
slider_ten_down		= board.get_pin('d:29:o')
slider_eleven_enable	= board.get_pin('d:6:p')
slider_eleven_up	= board.get_pin('d:31:o')
slider_eleven_down	= board.get_pin('d:33:o')
slider_twelve_enable	= board.get_pin('d:7:p')
slider_twelve_up	= board.get_pin('d:35:o')
slider_twelve_down	= board.get_pin('d:37:o')
slider_thirteen_enable	= board.get_pin('d:3:p')
slider_thirteen_up	= board.get_pin('d:41:o')
slider_thirteen_down	= board.get_pin('d:39:o')
slider_fourteen_enable	= board.get_pin('d:2:p')
slider_fourteen_up	= board.get_pin('d:45:o')
slider_fourteen_down	= board.get_pin('d:43:o')
slider_fifteen_enable	= board.get_pin('d:16:o')
slider_fifteen_up	= board.get_pin('d:49:o')
slider_fifteen_down	= board.get_pin('d:47:o')
slider_sixteen_enable	= board.get_pin('d:17:o')
slider_sixteen_up	= board.get_pin('d:53:o')
slider_sixteen_down	= board.get_pin('d:51:o')

#targetValue = float(input("Please enter a target value 0-9:  "))
#targetValue = targetValue/10

slider1_targetValue = 0.7
slider2_targetValue = 0.8
slider3_targetValue = .33
slider4_targetValue = .2
slider5_targetValue = .7
slider6_targetValue = .4
slider7_targetValue = .9
slider8_targetValue = .3
slider9_targetValue = .7
slider10_targetValue = .3
slider11_targetValue = .9
slider12_targetValue = .7
slider13_targetValue = .4
slider14_targetValue = .2
slider15_targetValue = .9
slider16_targetValue = .9

while True:
#    print("Desired position: ", targetValue)

     slider1 = slider_one.read()
     slider2 = slider_two.read()
     slider3 = slider_three.read()
     slider4 = slider_four.read()
     slider5 = slider_five.read()
     slider6 = slider_six.read()
     slider7 = slider_seven.read()
     slider8 = slider_eight.read()
     slider9 = slider_nine.read()
     slider10 = slider_ten.read()
     slider11 = slider_eleven.read()
     slider12 = slider_twelve.read()
     slider13 = slider_thirteen.read()
     slider14 = slider_fourteen.read()
     slider15 = slider_fifteen.read()
     slider16 = slider_sixteen.read()

     print("Slider 1:   ", slider1)
     print("Slider 2:   ", slider2)
     print("Slider 3:   ", slider3)
     print("Slider 4:   ", slider4)
     print("Slider 5:   ", slider5)
     print("Slider 6:   ", slider6)
     print("Slider 7:   ", slider7)
     print("Slider 8:   ", slider8)
     print("Slider 9:   ", slider9)
     print("Slider 10:  ", slider10)
     print("Slider 11:  ", slider11)
     print("Slider 12:  ", slider12)
     print("Slider 13:  ", slider13)
     print("Slider 14:  ", slider14)
     print("Slider 15:  ", slider15)
     print("Slider 16:  ", slider16)

     if (slider1 - slider1_targetValue) > threshold and (slider1 > slider1_targetValue):
        slider_one_up.write(0)
        slider_one_down.write(1)
        slider_one_enable.write(speed)
        slider_one_enable.write(0)
     elif (slider1_targetValue - slider1) > threshold and (slider1 < slider1_targetValue):
        slider_one_up.write(1)
        slider_one_down.write(0)
        slider_one_enable.write(speed)
     else:
        slider_one_enable.write(0)

     if (slider2 - slider2_targetValue) > threshold and (slider2 > slider2_targetValue):
        slider_two_up.write(0)
        slider_two_down.write(1)
        slider_two_enable.write(speed)
     elif (slider2_targetValue - slider2) > threshold and (slider2 < slider2_targetValue):
        slider_two_up.write(1)
        slider_two_down.write(0)
        slider_two_enable.write(speed)
     else:
        slider_two_enable.write(0)

     if (slider3 - slider3_targetValue) > threshold and (slider3 > slider3_targetValue):
        slider_three_up.write(0)
        slider_three_down.write(1)
        slider_three_enable.write(speed)
     elif (slider3_targetValue - slider3) > threshold and (slider3 < slider3_targetValue):
        slider_three_up.write(1)
        slider_three_down.write(0)
        slider_three_enable.write(speed)
     else:
        slider_three_enable.write(0)

     if (slider4 - slider4_targetValue) > threshold and (slider4 > slider4_targetValue):
        slider_four_up.write(0)
        slider_four_down.write(1)
        slider_four_enable.write(speed)
     elif (slider4_targetValue - slider4) > threshold and (slider4 < slider4_targetValue):
        slider_four_up.write(1)
        slider_four_down.write(0)
        slider_four_enable.write(speed)
     else:
        slider_four_enable.write(0)

     if (slider5 - slider5_targetValue) > threshold and (slider5 > slider5_targetValue):
        slider_five_up.write(0)
        slider_five_down.write(1)
        slider_five_enable.write(speed)
     elif (slider5_targetValue - slider5) > threshold and (slider5 < slider5_targetValue):
        slider_five_up.write(1)
        slider_five_down.write(0)
        slider_five_enable.write(speed)
     else:
        slider_five_enable.write(0)

     if (slider6 - slider6_targetValue) > threshold and (slider6 > slider6_targetValue):
        slider_six_up.write(0)
        slider_six_down.write(1)
        slider_six_enable.write(speed)
     elif (slider6_targetValue - slider6) > threshold and (slider6 < slider6_targetValue):
        slider_six_up.write(1)
        slider_six_down.write(0)
        slider_six_enable.write(speed)
     else:
        slider_six_enable.write(0)

#    if (slider7 - slider7_targetValue) > threshold and (slider7 > slider7_targetValue):
#       slider_seven_up.write(0)
#       slider_seven_down.write(1)
#       slider_seven_enable.write(speed)
#    elif (slider7_targetValue - slider7) > threshold and (slider7 < slider7_targetValue):
#       slider_seven_up.write(1)
#       slider_seven_down.write(0)
#       slider_seven_enable.write(speed)
#    else:
#       slider_seven_enable.write(0)

#    if (slider8 - slider8_targetValue) > threshold and (slider8 > slider8_targetValue):
#       slider_eight_up.write(0)
#       slider_eight_down.write(1)
#       slider_eight_enable.write(speed)
#    elif (slider8_targetValue - slider8) > threshold and (slider8 < slider8_targetValue):
#       slider_eight_up.write(1)
#       slider_eight_down.write(0)
#       slider_eight_enable.write(speed)
#    else:
#       slider_eight_enable.write(0)

     if (slider9 - slider9_targetValue) > threshold and (slider9 > slider9_targetValue):
        slider_nine_up.write(0)
        slider_nine_down.write(1)
        slider_nine_enable.write(speed)
     elif (slider9_targetValue - slider9) > threshold and (slider9 < slider9_targetValue):
        slider_nine_up.write(1)
        slider_nine_down.write(0)
        slider_nine_enable.write(speed)
     else:
        slider_nine_enable.write(0)

#    if (slider10 - slider10_targetValue) > threshold and (slider10 > slider10_targetValue):
#       slider_ten_up.write(0)
#       slider_ten_down.write(1)
#       slider_ten_enable.write(speed)
#    elif (slider10_targetValue - slider10) > threshold and (slider10 < slider10_targetValue):
#       slider_ten_up.write(1)
#       slider_ten_down.write(0)
#       slider_ten_enable.write(speed)
#    else:
#       slider_ten_enable.write(0)

#    if (slider11 - slider11_targetValue) > threshold and (slider11 > slider11_targetValue):
#       slider_eleven_up.write(0)
#       slider_eleven_down.write(1)
#       slider_eleven_enable.write(speed)
#    elif (slider11_targetValue - slider11) > threshold and (slider11 < slider11_targetValue):
#       slider_eleven_up.write(1)
#       slider_eleven_down.write(0)
#       slider_eleven_enable.write(speed)
#    else:
#       slider_eleven_enable.write(0)

     if (slider12 - slider12_targetValue) > threshold and (slider12 > slider12_targetValue):
        slider_twelve_up.write(0)
        slider_twelve_down.write(1)
        slider_twelve_enable.write(speed)
     elif (slider12_targetValue - slider12) > threshold and (slider12 < slider12_targetValue):
        slider_twelve_up.write(1)
        slider_twelve_down.write(0)
        slider_twelve_enable.write(speed)
     else:
        slider_twelve_enable.write(0)

#    if (slider13 - slider13_targetValue) > threshold and (slider13 > slider13_targetValue):
#       slider_thirteen_up.write(0)
#       slider_thirteen_down.write(1)
#       slider_thirteen_enable.write(speed)
#    elif (slider13_targetValue - slider13) > threshold and (slider13 < slider13_targetValue):
#       slider_thirteen_up.write(1)
#       slider_thirteen_down.write(0)
#       slider_thirteen_enable.write(speed)
#    else:
#       slider_thirteen_enable.write(0)

     if (slider14 - slider14_targetValue) > threshold and (slider14 > slider14_targetValue):
        slider_fourteen_up.write(0)
        slider_fourteen_down.write(1)
        slider_fourteen_enable.write(speed)
     elif (slider14_targetValue - slider14) > threshold and (slider14 < slider14_targetValue):
        slider_fourteen_up.write(1)
        slider_fourteen_down.write(0)
        slider_fourteen_enable.write(speed)
     else:
        slider_fourteen_enable.write(0)

     if (slider15 - slider15_targetValue) > threshold and (slider15 > slider15_targetValue):
        slider_fifteen_up.write(0)
        slider_fifteen_down.write(1)
        slider_fifteen_enable.write(speed)
     elif (slider15_targetValue - slider15) > threshold and (slider15 < slider15_targetValue):
        slider_fifteen_up.write(1)
        slider_fifteen_down.write(0)
        slider_fifteen_enable.write(speed)
     else:
        slider_fifteen_enable.write(0)

     if (slider16 - slider16_targetValue) > threshold and (slider16 > slider16_targetValue):
        slider_sixteen_up.write(0)
        slider_sixteen_down.write(1)
        slider_sixteen_enable.write(speed)
     elif (slider16_targetValue - slider16) > threshold and (slider16 < slider16_targetValue):
        slider_sixteen_up.write(1)
        slider_sixteen_down.write(0)
        slider_sixteen_enable.write(speed)
     else:
        slider_sixteen_enable.write(0)


     clear() 
board.exit()

