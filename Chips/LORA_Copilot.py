import time
import machine
from lora import LoRa

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

# Enviar algunos datos
s.send(bytes([0x01, 0x02, 0x03]))

print('¡Datos enviados!')
