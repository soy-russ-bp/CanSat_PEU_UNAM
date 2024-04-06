import time
import math
import board
import busio
import adafruit_icm20x

# Inicializar I2C bus y sensor.
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_icm20x.ICM20948(i2c)

def recibir_datos():
    # Leer y devolver los datos del acelerómetro y el giroscopio.
    aceleracion = sensor.acceleration
    giroscopio = sensor.gyro
    return aceleracion, giroscopio

while True:
    # Recibir datos del sensor.
    aceleracion, giroscopio = recibir_datos()
    
    # Convertir los datos del giroscopio a grados.
    giroscopio_grados = [math.degrees(x) for x in giroscopio]
    
    # Imprimir los datos del acelerómetro y el giroscopio.
    print("Acelerómetro: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % aceleracion)
    print("Giroscopio: X:%.2f, Y: %.2f, Z: %.2f grados" % tuple(giroscopio_grados))
    
    # Esperar un segundo antes de la próxima lectura.
    time.sleep(1)
