import machine
import time

class SensorDistancia:
    def __init__(self):
        self.adc = machine.ADC(26)  # GP26 es el único pin ADC en la Raspberry Pi Pico

    def leer_distancia(self):
        # Leer el valor del ADC
        valor_adc = self.adc.read_u16()

        # Convertir el valor del ADC a voltaje
        voltaje = valor_adc * 3.3 / 65535

        # Convertir el voltaje a distancia (cm)
        distancia = 27.86 * (voltaje ** -1.15)

        return distancia

    def imprimir_distancia(self):
        while True:
            distancia = self.leer_distancia()
            print("Distancia: %.2f cm" % distancia)
            time.sleep(1)

# Crear una instancia de la clase SensorDistancia
sensor = SensorDistancia()

# Llamar al método imprimir_distancia
sensor.imprimir_distancia()
