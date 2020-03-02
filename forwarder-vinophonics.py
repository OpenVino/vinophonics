import json
import web3
import time

from web3 import Web3, HTTPProvider

print("\n1) Connecting to the costaflores-node2 (http://10.112.48.25:8547) ...")

w3 = Web3(HTTPProvider("http://10.112.48.25:8547"))

print("2) Preparing contracts (Datastorage)...")

with open('contracts.json') as json_file:
    compiled_sol = json.load(json_file)

contract = w3.eth.contract(address = w3.toChecksumAddress("0x864d6819946dF8a763454627342bb3A7a2692805"), abi = compiled_sol['contracts']['contracts.sol:Datastorage']['abi'], )

print("\n ================================================== \n")

def handle_event(event):

    receipt = w3.eth.waitForTransactionReceipt(event['transactionHash'])
    result = contract.events.DataInserted().processReceipt(receipt)


    # THIS IS NOT NEEDED, JUST TO CHECK CONSOLE
    print("[" + result[0]['args']['_identifier'].decode('utf-8') + "] : {" +
    "  sensor2: " + str(contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 0).call()/100) +
    ", sensor1: " + str(contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 1).call()/100) +
    ", sensor05: " + str(contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 2).call()/100) +
    ", sensor005: " + str(contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 3).call()/100) +
    ", battery: " + str(contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 4).call()/100) +
    ", temperature: " + str(contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 5).call()/100) +
    ", wind_speed: " + str(contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 7).call()/100) +
    ", wind_gust: " + str(contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 8).call()/100) +
    ", wind_direction: " + str(contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 9).call()/100) +
    ", pressure: " + str(contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 10).call()/100) +
    ", rain: " + str(contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 11).call()/100) +
    ", temperature: " + str(contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 12).call()/100) +
    ", humidity: " + str(contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 13).call()/100)
    + "}");

    id = result[0]['args']['_identifier'].decode('utf-8')

    # => Sensor specific data.
    sensor2 = contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 0).call()/100
    sensor1 = contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 1).call()/100
    sensor05 = contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 2).call()/100
    sensor005 = contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 3).call()/100
    battery = contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 4).call()/100
    temperature = contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 5).call()/100

    # => Weather station data. (global data)
    wind_speed = contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 7).call()/100
    wind_gust = contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 8).call()/100
    wind_direction = contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 9).call()/100
    pressure = contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 10).call()/100
    rain = contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 11).call()/100
    temperature = contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 12).call()/100
    humidity = contract.functions.data(result[0]['args']['_identifier'].decode('utf-8').encode('utf-8'), 13).call()/100

    # Add communication with Vinophonics here, to do:

    # data = ... TREAT DATA HERE AS STRING
    # file = open("/var/tmp/data.txt", data)

def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
            time.sleep(poll_interval)

block_filter = w3.eth.filter({'fromBlock':'latest'})
log_loop(block_filter, 2)
