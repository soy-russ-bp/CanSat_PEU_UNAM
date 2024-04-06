import machine
import time

# Configurar el pin ADC
adc = machine.ADC(26)  # GP26 es el único pin ADC en la Raspberry Pi Pico

def leer_distancia():
    # Leer el valor del ADC
    valor_adc = adc.read_u16()

    # Convertir el valor del ADC a voltaje
    voltaje = valor_adc * 3.3 / 65535

    # Convertir el voltaje a distancia (cm)
    distancia = 27.86 * (voltaje ** -1.15)

    return distancia

while True:
    distancia = leer_distancia()
    print("Distancia: %.2f cm" % distancia)
    time.sleep(1)
