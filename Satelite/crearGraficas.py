import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import datetime

def crear_grafica(canvas, posicion, nombre_base_archivo, generador_datos, max_x=10, max_y=100):
    figura = plt.Figure(figsize=(4, 2.7), dpi=100)  # Ajusta el tamaño de la figura según necesites
    subplot = figura.add_subplot(111)
    subplot.set_ylim(0, max_y)

    canvas_figura = FigureCanvasTkAgg(figura, master=canvas)
    widget_figura = canvas_figura.get_tk_widget()
    canvas.create_window(posicion, window=widget_figura, anchor="nw")

    datos_x, datos_y = [], []

    # Asegúrate de tener esta línea para crear el directorio de datos si no existe
    os.makedirs('datos_graficas', exist_ok=True)
    archivo_datos_path = os.path.join('datos_graficas', f'{nombre_base_archivo}.txt')

    def actualizar(i):
        # Obtener nuevos datos del generador
        hora_actual, valor = generador_datos()

        datos_x.append(hora_actual)
        datos_y.append(valor)

        with open(archivo_datos_path, 'a') as archivo_datos:
            archivo_datos.write(f"{hora_actual}, {valor}\n")

        # Mantener un número limitado de datos
        if len(datos_x) > max_x:
            datos_x.pop(0)
            datos_y.pop(0)

        subplot.clear()
        subplot.plot(datos_x, datos_y)
        subplot.set_ylim(0, max_y)
        # Configura aquí el eje x si es necesario, por ejemplo, para manejar fechas/horas adecuadamente

    ani = FuncAnimation(figura, actualizar, interval=1000, cache_frame_data=False)

    return canvas_figura, ani

# Ejemplo de uso
# Deberás reemplazar 'tu_canvas' y 'tu_posicion' por los valores adecuados para tu caso
# generador_datos_fake es un ejemplo de cómo podría ser tu función generadora de datos
import random

def generador_datos_fake(max_y=100):
    hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
    valor_random = random.randint(0, max_y)  # Asumiendo max_y=100
    return hora_actual, valor_random

