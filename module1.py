import time
from pyfirmata import Arduino, util

# use 'pin#' .write(1) for high, .write(0) for low

board = Arduino("COM3")

pump_1 = board.get_pin('d:3:o') # pin 3 connects to first relay -> first pump
pump_2 = board.get_pin('d:4:o') # pin 4 connects to second relay -> second pump
pump_3 = board.get_pin('d:5:o') # pin 5 connects to third relay -> third pump

def vodka_sprite():
    pump_1.write(1)
    time.sleep(3)
    pump_1.write(0)
    pump_2.write(1)
    time.sleep(3)
    pump_2.write(0)

def john_daley():
    pump_1.write(1)
    time.sleep(4)
    pump_1.write(0)
    pump_2.write(1)
    
    time.sleep(4)
    pump_2.write(0)
    pump_3.write(1)
    time.sleep(4)
    pump_3.write(0)
