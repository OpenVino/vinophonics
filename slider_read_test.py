#!/usr/bin/env python3
import time
import pyfirmata
board = pyfirmata.ArduinoMega('/dev/ttyACM0')  # arduino setup

# import only system from os 
from os import system, name 
from decimal import Decimal

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

while True:

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

     print( "Slider 1:   ", slider1)
     print( "Slider 2:   ", slider2)
     print( "Slider 3:   ", slider3)
     print( "Slider 4:   ", slider4)
     print( "Slider 5:   ", slider5)
     print( "Slider 6:   ", slider6)
     print( "Slider 7:   ", slider7)
     print( "Slider 8:   ", slider8)
     print( "Slider 9:   ", slider9)
     print( "Slider 10:  ", slider10)
     print( "Slider 11:  ", slider11)
     print( "Slider 12:  ", slider12)
     print( "Slider 13:  ", slider13)
     print( "Slider 14:  ", slider14)
     print( "Slider 15:  ", slider15)
     print( "Slider 16:  ", slider16)


     time.sleep(1)

     clear() 
board.exit()

