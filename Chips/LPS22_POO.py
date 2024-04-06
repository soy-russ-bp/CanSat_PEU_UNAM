import time
import machine
import lps22

class SensorLPS22:
    def __init__(self):
        self.i2c = machine.I2C(0)
        self.sensor = lps22.LPS22(self.i2c)

    def leer_temperatura(self):
        # Leer datos de temperatura
        temperatura = self.sensor.temperature
        return temperatura

    def leer_presion(self):
        # Leer datos de presión
        presion = self.sensor.pressure
        return presion

    def imprimir_datos(self):
        while True:
            print("Temperatura: %.2f C" % self.leer_temperatura())
            print("Presión: %.2f hPa" % self.leer_presion())
            time.sleep(1)

# Crear una instancia de la clase SensorLPS22
sensor = SensorLPS22()

# Llamar al método imprimir_datos
sensor.imprimir_datos()
