import time
import board
import busio
import adafruit_shtc3

# Inicializar I2C bus y sensor.
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_shtc3.SHTC3(i2c)

while True:
    # Leer y devolver los datos de temperatura y humedad.
    temperatura, humedad = sensor.measurements
    
    # Imprimir los datos de temperatura y humedad.
    print("Temperatura: %.2f C" % temperatura)
    print("Humedad: %.2f %% RH" % humedad)
    
    # Esperar un segundo antes de la próxima lectura.
    time.sleep(1)
