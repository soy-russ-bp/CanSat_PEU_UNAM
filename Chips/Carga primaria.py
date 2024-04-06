import time
import machine
import shtc3
import lps22

# Inicializar I2C y los sensores
i2c = machine.I2C(0)
sensor_shtc3 = shtc3.SHTC3(i2c)
sensor_lps22 = lps22.LPS22(i2c)

def leer_datos_shtc3():
    # Leer datos de temperatura y humedad del sensor SHTC3
    temperatura, humedad = sensor_shtc3.measurements
    return temperatura, humedad

def leer_datos_lps22():
    # Leer datos de temperatura y presión del sensor LPS22
    temperatura = sensor_lps22.temperature
    presion = sensor_lps22.pressure
    return temperatura, presion

def imprimir_datos():
    while True:
        temperatura_shtc3, humedad = leer_datos_shtc3()
        temperatura_lps22, presion = leer_datos_lps22()
        print("Temperatura SHTC3: %.2f C" % temperatura_shtc3)
        print("Humedad: %.2f %% RH" % humedad)
        print("Temperatura LPS22: %.2f C" % temperatura_lps22)
        print("Presión: %.2f hPa" % presion)
        time.sleep(1)

# Llamar a la función imprimir_datos
imprimir_datos()
