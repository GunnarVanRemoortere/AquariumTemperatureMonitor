import RPi.GPIO as GPIO
import dht11
import time
import ds18b20Klasse
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=14)
onewire = ds18b20Klasse.DS18B20Class()
while True:
    result = instance.read()
    result2 = onewire.geefTemperaturen()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
    if result2 != 0:
        print("Temperature: %d" % result2)
    time.sleep(1)
