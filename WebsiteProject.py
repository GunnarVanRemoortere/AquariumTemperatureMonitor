from flask import Flask
from flask import render_template
from DbClass import DbClass
import dht11
import ds18b20Klasse
import os

app = Flask(__name__)


def roundValue(x, base=5):
    return int(base * round(float(x) / base))


@app.route('/')
def Home():

    #vochtigheid inlezen
    humiditysensor = dht11.DHT11(pin=14)
    humidity = humiditysensor.read().humidity
    vochtigheidsWaarde = roundValue(humidity)

    #temperatuur dht11 inlezen
    temperature = humiditysensor.read().temperature
    temperatureWaarde = roundValue(temperature)

    #temperatuur ds18b20 inlezen
    waterTemperatureSensor = ds18b20Klasse.DS18B20Class
    waterTemperature = waterTemperatureSensor.geefTemperaturen()

    return render_template('Home.html', humidityWaarde=vochtigheidsWaarde, waterTemp=waterTemperature, temp=temperatureWaarde)


@app.route('/Data')
def Data():
    instantieDb = DbClass()
    waterTemperature = instantieDb.getTemperatuurWater()

    vochtigheidsWaarde = instantieDb.getLuchvochtigheid()

    temperatuurWaarde = instantieDb.getTemperatuurOmgeving()

    tijd = instantieDb.getTijd()

    return render_template('Data.html', waterTemp=waterTemperature, humidityWaarde=vochtigheidsWaarde, temp=temperatuurWaarde, tijdwaarden=tijd)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    host = "169.254.10.1"
    app.run(host=host, port=port, debug=True)
