import time
import machine
import shtc3
import lps22
from lora import LoRa

# Inicializar I2C y los sensores
i2c = machine.I2C(0)
sensor_shtc3 = shtc3.SHTC3(i2c)
sensor_lps22 = lps22.LPS22(i2c)

# Configuración del módulo LoRa
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.US915)

# Configuración de los canales
for channel in range(0, 72):
    lora.remove_channel(channel)
for channel in range(903900000, 914700000, 200000):
    lora.add_channel(channel)

# Configuración de las claves de red y de aplicación
app_eui = '70B3D57ED00001A6'
app_key = 'A23C96EE13804963F8C2BD6285448198'

# Unirse a la red LoRaWAN
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# Esperar a que se complete la unión a la red
while not lora.has_joined():
    time.sleep(2.5)
    print('Esperando a unirse a la red...')

print('¡Unido a la red!')

# Crear un socket LoRaWAN
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# Configurar el modo de operación del socket
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

def leer_datos_shtc3():
    # Leer datos de temperatura y humedad del sensor SHTC3
    temperatura, humedad = sensor_shtc3.measurements
    return temperatura, humedad

def leer_datos_lps22():
    # Leer datos de temperatura y presión del sensor LPS22
    temperatura = sensor_lps22.temperature
    presion = sensor_lps22.pressure
    return temperatura, presion

def enviar_datos():
    while True:
        temperatura_shtc3, humedad = leer_datos_shtc3()
        temperatura_lps22, presion = leer_datos_lps22()
        datos = bytes([temperatura_shtc3, humedad, temperatura_lps22, presion])
        s.send(datos)
        print('¡Datos enviados!')
        time.sleep(1)

# Llamar a la función enviar_datos
enviar_datos()
