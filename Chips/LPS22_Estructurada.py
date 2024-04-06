import time
import machine
import lps22

# Inicializar I2C y el sensor
i2c = machine.I2C(0)
sensor = lps22.LPS22(i2c)

def leer_temperatura():
    # Leer datos de temperatura
    temperatura = sensor.temperature
    return temperatura

def leer_presion():
    # Leer datos de presión
    presion = sensor.pressure
    return presion

def imprimir_datos():
    while True:
        print("Temperatura: %.2f C" % leer_temperatura())
        print("Presión: %.2f hPa" % leer_presion())
        time.sleep(1)

# Llamar a la función imprimir_datos
imprimir_datos()

