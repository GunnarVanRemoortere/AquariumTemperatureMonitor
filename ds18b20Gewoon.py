import time

#id van one-wire sensor opzoeken
sensor_file = '/sys/bus/w1/devices/28-0316616335ff/w1_slave'

def read_temp_raw():
    with open(sensor_file, 'r') as f:
        lines = f.readlines()
    return lines

def read_temp():
    lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        lijn = lines[1]
        temperature = float(lijn[29:])/1000
        return temperature

while True:
    print("Het is: " + str(read_temp()) +  " graden Celsius")
    time.sleep(1)
