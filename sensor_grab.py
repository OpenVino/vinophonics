#!/usr/bin/python3

import time
import json
import requests
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# Set the LED GPIO number
LED = 17

# Set the LED GPIO pin as an output
GPIO.setup(LED, GPIO.OUT)

# Set the "local-blockchain-remote" GPIO pin as an output
GPIO.setup(22, GPIO.IN) # REMOTE
GPIO.setup(23, GPIO.IN) # LOCAL

# Define default hash values
cab_hash = 0
petit_hash = 0
mw_hash = 0
me_hash = 0

while True:

	try:
		r = requests.get('http://costaflores.openvino.exchange/now')
		r_list= r.json()

		cabernet = (r_list[0])
		petit_verdot = (r_list[1])
		malbec_oeste = (r_list[2])
		malbec_este = (r_list[3])
		
		cs_hash = cabernet["hash"]
		pv_hash = petit_verdot["hash"]
		mbo_hash = malbec_oeste["hash"]
		mbe_hash = malbec_este["hash"]
	except:
		print("no connection?")

	if GPIO.input(23) == 1:
		print ("Switch is set to LOCAL. Do nothing with CS. ")
	elif (cs_hash != cab_hash):
		cs_soil_2 = cabernet["humidity2"]
		cs_soil_1 = cabernet["humidity2"]
		cs_soil_05 = cabernet["humidity05"]
		cs_soil_005 = cabernet["humidity005"]
		cs_wind_vel = cabernet["wind_velocity"]
		cs_wind_gst = cabernet["wind_gust"]
		cs_wind_dir = cabernet["wind_direction"]
		cs_atm_prs = cabernet["pressure"]
		cs_rain = cabernet["rain"]
		#cs_light_vi = cabernet["light_vi"]
		#cs_light_uv = cabernet["light_uv"]
		#cs_light_ir = cabernet["light_ir"]
		cab_hash = cs_hash
		print("New Cabernet Sauvignon hash: ", cs_hash)
		GPIO.output(LED,True)
		time.sleep(.1)
		GPIO.output(LED,False)
	else: 
		print("Nothing new CS.")
		time.sleep(.1)

	if GPIO.input(23) == 1:
		print ("Switch is set to LOCAL. Do nothing with PV. ")
	elif (pv_hash != petit_hash):
		pv_soil_2 = petit_verdot["humidity2"]
		pv_soil_1 = petit_verdot["humidity2"]
		pv_soil_05 = petit_verdot["humidity05"]
		pv_soil_005 = petit_verdot["humidity005"]
		pv_wind_vel = petit_verdot["wind_velocity"]
		pv_wind_gst = petit_verdot["wind_gust"]
		pv_wind_dir = petit_verdot["wind_direction"]
		pv_atm_prs = petit_verdot["pressure"]
		pv_rain = petit_verdot["rain"]
		#pv_light_vi = petit_verdot["light_vi"]
		#pv_light_uv = petit_verdot["light_uv"]
		#pv_light_ir = petit_verdot["light_ir"]
		petit_hash = pv_hash
		print("New Petit Verdot hash: ", pv_hash)
		GPIO.output(LED,True)
		time.sleep(.1)
		GPIO.output(LED,False)
	else: 
		print("Nothing new PV.")
		time.sleep(.1)

	if GPIO.input(23) == 1:
		print ("Switch is set to LOCAL. Do nothing with MW. ")
	elif (mbo_hash != mw_hash):
		mbo_soil_2 = petit_verdot["humidity2"]
		mbo_soil_1 = petit_verdot["humidity2"]
		mbo_soil_05 = petit_verdot["humidity05"]
		mbo_soil_005 = petit_verdot["humidity005"]
		mbo_wind_vel = petit_verdot["wind_velocity"]
		mbo_wind_gst = petit_verdot["wind_gust"]
		mbo_wind_dir = petit_verdot["wind_direction"]
		mbo_atm_prs = petit_verdot["pressure"]
		mbo_rain = petit_verdot["rain"]
		#mbo_light_vi = petit_verdot["light_vi"]
		#mbo_light_uv = petit_verdot["light_uv"]
		#mbo_light_ir = petit_verdot["light_ir"]
		mw_hash = mbo_hash
		print("New Malbec West hash: ", mbo_hash)
		GPIO.output(LED,True)
		time.sleep(.1)
		GPIO.output(LED,False)
	else: 
		print("Nothing new MW.")
		time.sleep(.1)

	if GPIO.input(23) == 1:
		print ("Switch is set to LOCAL. Do nothing with ME. ")
	elif (mbe_hash != me_hash):
		mbe_soil_2 = petit_verdot["humidity2"]
		mbe_soil_1 = petit_verdot["humidity2"]
		mbe_soil_05 = petit_verdot["humidity05"]
		mbe_soil_005 = petit_verdot["humidity005"]
		mbe_wind_vel = petit_verdot["wind_velocity"]
		mbe_wind_gst = petit_verdot["wind_gust"]
		mbe_wind_dir = petit_verdot["wind_direction"]
		mbe_atm_prs = petit_verdot["pressure"]
		mbe_rain = petit_verdot["rain"]
		#mbe_light_vi = petit_verdot["light_vi"]
		#mbe_light_uv = petit_verdot["light_uv"]
		#mbe_light_ir = petit_verdot["light_ir"]
		me_hash = mbe_hash
		print("New Malbec East hash: ", mbe_hash)
		GPIO.output(LED,True)
		time.sleep(.1)
		GPIO.output(LED,False)
	else: 
		print("Nothing new ME.")
		time.sleep(.1)

