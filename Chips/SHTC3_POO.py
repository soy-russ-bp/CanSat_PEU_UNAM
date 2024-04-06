import time
import machine
import shtc3

import board
import busio
import adafruit_shtc3

class SensorSHTC3:
    def __init__(self):
        self.i2c = machine.I2C(0)
        self.sensor = shtc3.SHTC3(self.i2c)

    def leer_datos(self):
        temperatura, humedad = self.sensor.measurements
        return temperatura, humedad

    def imprimir_datos(self):
        while True:
            temperatura, humedad = self.leer_datos()
            print("Temperatura: %.2f C" % temperatura)
            print("Humedad: %.2f %% RH" % humedad)
            time.sleep(1)

# Crear una instancia de la clase SensorSHTC3
sensor = SensorSHTC3()

# Llamar al método imprimir_datos
sensor.imprimir_datos()


