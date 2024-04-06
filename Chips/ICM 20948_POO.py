from machine import Pin, I2C
from icm20948 import ICM20948
import utime

import time
import math
import board
import busio
import adafruit_icm20x

class SensorICM20948:
    def __init__(self):
        # Inicializar I2C bus y sensor.
        self.i2c = I2C(1, scl=Pin(27), sda=Pin(26), freq=400000)
        self.sensor = ICM20948(self.i2c)

    def recibir_datos(self):
        # recibe y devuelve los datos del acelerometro y el giroscopio
        aceleracion = self.sensor.acceleration
        giroscopio = self.sensor.gyro
        return aceleracion, giroscopio

    def imprimir_datos(self):
        while True:
            # recibe datos del sensor
            aceleracion, giroscopio = self.recibir_datos()
            
            # conversion de los datos del giroscopio a grados
            giroscopio_grados = [math.degrees(x) for x in giroscopio]
            
            # imrpime los datos del acelerometro y el giroscopio
            print("Acelerómetro: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % aceleracion)
            print("Giroscopio: X:%.2f, Y: %.2f, Z: %.2f grados" % tuple(giroscopio_grados))
            
            # esperar un segundo antes de la proxima lectura
            time.sleep(1)

# crea una instancia de la clase SensorICM20948
sensor = SensorICM20948()

# llamada del metodo imprimir_datos del ICM
sensor.imprimir_datos()

