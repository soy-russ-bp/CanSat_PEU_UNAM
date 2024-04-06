import time
import machine
import socket
import shtc3
import lps22
from lora import LoRa

# Inicializar I2C y los sensores
i2c = machine.I2C(0)
sensor_shtc3 = shtc3.SHTC3(i2c)
sensor_lps22 = lps22.LPS22(i2c)

# Configuración del módulo LoRa
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.US915)

# Asumiendo que la configuración de canales y unión está correcta para tu dispositivo y región
# Unirse a la red LoRaWAN (asegúrate de que los EUI y KEY sean los correctos y estén en formato de bytes si es necesario)

# Esperar a que se complete la unión a la red
while not lora.has_joined():
    time.sleep(2.5)
    print('Esperando a unirse a la red...')

print('¡Unido a la red!')

# Crear un socket LoRaWAN
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

def leer_datos_shtc3():
    temperatura, humedad = sensor_shtc3.measurements()
    return temperatura, humedad

def leer_datos_lps22():
    temperatura = sensor_lps22.temperature()
    presion = sensor_lps22.pressure()
    return temperatura, presion

def enviar_datos():
    while True:
        temp_shtc3, humedad = leer_datos_shtc3()
        temp_lps22, presion = leer_datos_lps22()
        
        # Preparar los datos para enviar
        # Aquí se asume que la conversión a un formato adecuado para enviar como bytes, puede ser necesario ajustar dependiendo de los rangos de tus datos
        datos = bytearray()
        datos.extend(int(temp_shtc3 * 100).to_bytes(2, 'big'))  # Ejemplo de conversión a centígrados * 100 para mantener dos decimales
        datos.extend(int(humedad * 100).to_bytes(2, 'big'))
        datos.extend(int(temp_lps22 * 100).to_bytes(2, 'big'))
        datos.extend(int(presion).to_bytes(4, 'big'))  # Asumiendo que la presión se puede representar como un entero
        
        s.send(datos)
        print('¡Datos enviados!')
        time.sleep(60)  # Esperar un minuto antes de enviar el siguiente conjunto de datos

# Llamar a la función enviar_datos
enviar_datos()
