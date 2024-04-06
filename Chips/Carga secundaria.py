import time
import machine
import shtc3
import lps22
from icm20948 import ICM20948
import math

class SensorSHTC3:
    def __init__(self):
        self.i2c = machine.I2C(0)
        self.sensor = shtc3.SHTC3(self.i2c)

    def leer_datos(self):
        temperatura, humedad = self.sensor.measurements
        return temperatura, humedad

class SensorICM20948:
    def __init__(self):
        self.i2c = machine.I2C(1)
        self.sensor = ICM20948(self.i2c)

    def recibir_datos(self):
        aceleracion = self.sensor.acceleration
        giroscopio = self.sensor.gyro
        return aceleracion, giroscopio

class SensorLPS22:
    def __init__(self):
        self.i2c = machine.I2C(0)
        self.sensor = lps22.LPS22(self.i2c)

    def leer_temperatura(self):
        temperatura = self.sensor.temperature
        return temperatura

    def leer_presion(self):
        presion = self.sensor.pressure
        return presion

class SensorDistancia:
    def __init__(self):
        self.adc = machine.ADC(26)  # GP26 es el único pin ADC en la Raspberry Pi Pico

    def leer_distancia(self):
        valor_adc = self.adc.read_u16()
        voltaje = valor_adc * 3.3 / 65535
        distancia = 27.86 * (voltaje ** -1.15)
        return distancia

def imprimir_datos():
    sensor_shtc3 = SensorSHTC3()
    sensor_icm20948 = SensorICM20948()
    sensor_lps22 = SensorLPS22()
    sensor_distancia = SensorDistancia()

    while True:
        temperatura_shtc3, humedad = sensor_shtc3.leer_datos()
        aceleracion, giroscopio = sensor_icm20948.recibir_datos()
        giroscopio_grados = [math.degrees(x) for x in giroscopio]
        temperatura_lps22 = sensor_lps22.leer_temperatura()
        presion = sensor_lps22.leer_presion()
        distancia = sensor_distancia.leer_distancia()

        print("Temperatura SHTC3: %.2f C" % temperatura_shtc3)
        print("Humedad: %.2f %% RH" % humedad)
        print("Acelerómetro: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % aceleracion)
        print("Giroscopio: X:%.2f, Y: %.2f, Z: %.2f grados" % tuple(giroscopio_grados))
        print("Temperatura LPS22: %.2f C" % temperatura_lps22)
        print("Presión: %.2f hPa" % presion)
        print("Distancia entre cargas: %.2f cm" % distancia)

        time.sleep(1)

# Llamar a la función imprimir_datos
imprimir_datos()
