from DbClass import DbClass
import dht11
import ds18b20Klasse
from time import sleep

db = DbClass()
humiditysensor = dht11.DHT11(pin=14)
onewire = ds18b20Klasse.DS18B20Class

def wegschrijvenVanSensorenNaarDb():
    humidityWaarde = humiditysensor.read().humidity

    temperatureWater = onewire.geefTemperaturen()

    temperature = humiditysensor.read().temperature

    db.setDataToDatabase(temperature, temperatureWater, humidityWaarde)

try:
    count = 0
    while 1:
        wegschrijvenVanSensorenNaarDb()
        count += 1
        print(count)
except KeyboardInterrupt:
    print("End")

