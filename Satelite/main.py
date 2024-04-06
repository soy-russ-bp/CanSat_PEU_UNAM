import datetime
import random
import tkinter as tk
from PIL import Image, ImageTk
import crearGraficas as gr
import estilos as est

# Inicialización de la ventana de Tkinter
ventana = tk.Tk()
ventana.title("Control satelital")
# Ajustar la ventana a pantalla completa
est.pantalla_completa(ventana) 

# Ajustar la ventana a las dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Cargar y establecer la imagen de fondo
ruta_imagen = "temple-kukulkan.jpeg"
imagen = Image.open(ruta_imagen)
ancho_rectangulo = 450  # Ajusta esto según necesites, es del rectángulo de datos

# Ajustar el tamaño del fondo para ocupar todo menos el espacio del rectángulo blanco
imagen_duplicada = imagen.resize((ancho_pantalla - ancho_rectangulo, alto_pantalla))
foto = ImageTk.PhotoImage(imagen_duplicada)

canvas = tk.Canvas(ventana, width=ancho_pantalla, height=alto_pantalla)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor="nw", image=foto)

# Crear rectángulo blanco en el lado derecho
canvas.create_rectangle(ancho_pantalla - ancho_rectangulo, 0, ancho_pantalla, alto_pantalla, fill="white")

# Posiciones para las gráficas en el canvas
posiciones = [(50, 170), (520, 170), (50, 530), (520, 530)]

# Lista para mantener las referencias de las animaciones
animaciones = []
nombres_graficas = ['presion', 'temperatura', 'velocidad', 'aceleracion']
max_y = 100  # Ajusta esto según tus necesidades

for nombre, posicion in zip(nombres_graficas, posiciones):
    canvas_figura, ani = gr.crear_grafica(canvas, posicion, nombre, max_x=100, max_y=max_y)
    animaciones.append(ani) 

# Asegúrate de ajustar la creación de gráficas y otros elementos dinámicamente con estas nuevas dimensiones y posiciones.

# Añadir texto al rectángulo blanco

# Crear StringVars para los datos
tiempo_var = tk.StringVar(value="XX")
altura_var = tk.StringVar(value="XX")
latitud_var = tk.StringVar(value="XX")
longitud_var = tk.StringVar(value="XX")
distancia_var = tk.StringVar(value="XX")
orientacion_var = tk.StringVar(value="XX")
rotacion_var = tk.StringVar(value="XX")
angulo_carga_var = tk.StringVar(value="XX")

# Colocar las etiquetas y los datos en el canvas
label_tiempo = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 60, "Tiempo:", tiempo_var)
label_altura = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 120, "Altura:", altura_var)

label_carga_secundaria = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 100, 210-30, "Carga secundaria:", None, True)

label_latitud = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 240-30, "Latitud:", latitud_var)
label_longitud = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 270-30, "Longitud:", latitud_var)
label_distancia = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 300-30, "Distancia respecto C1:", latitud_var)

label_orientacion = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 330, "Orientación Carga Primaria:", None, True)
label_latitud = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 360, "Latitud:", latitud_var)
label_longitud = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 390, "Longitud:", latitud_var)

label_rotacion = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 420, "Rotación:", None)
label_eje_x = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 450, "Eje X:", latitud_var)
label_eje_y = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 480, "Eje Y:", latitud_var)
label_eje_z = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 510, "Eje Z:", latitud_var)

label_angulo_carga = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 570, "Ángulo Respecto C2:", latitud_var)
# Repite para otros datos según necesites

# Crear logo y título de Ka'an Astra
 # Cargar y mostrar el logo en la parte superior izquierda
ruta_logo = "logo.png" 
logo = Image.open(ruta_logo)
logo = logo.resize((90, 90))
foto_logo = ImageTk.PhotoImage(logo)
canvas.create_image(20, 10, anchor="nw", image=foto_logo)  # Ajusta las coordenadas según necesites

    # Cargar y mostrar el titulo en la parte superior izquierda
ruta_titulo = "titulo.png" 
titulo = Image.open(ruta_titulo)
foto_titulo = ImageTk.PhotoImage(titulo)
canvas.create_image(150, 10, anchor="nw", image=foto_titulo)  # Ajusta las coordenadas según necesites

# Crear títulos con bordes redondeados de todas las gráficas
est.pack_titulos(canvas)

# Crear botones en el lado izquierdo
est.pack_botones(ventana, canvas, 294 , 815, est.inicioRecoleccionDatos, est.exportar_datos, est.finRecoleccionDatos)

est.minimun_size(ventana, 1200, 800 )

ventana.mainloop()
