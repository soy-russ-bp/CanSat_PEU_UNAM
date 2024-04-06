
import random
import tkinter as tk
from PIL import Image, ImageTk
import crearGraficas as gr
import estilos as est

def actualizar_labels():
    # Actualizar el tiempo
    tiempo_actual = float(tiempo_var.get())
    if int(tiempo_actual) % 60 == 0 and tiempo_actual % 1.0 == 0.0:  # Cada 60 segundos
        tiempo_var.set(f"{tiempo_actual - 0.9 + 1.0:.1f}")
    else:
        tiempo_var.set(f"{tiempo_actual + 0.1:.1f}")
    
    # Actualizar otros datos con valores aleatorios como ejemplo
    altura_var.set(f"{random.randint(0, 400)}")
    
    latitudc2_var.set(f"{random.uniform(-90, 90):.2f}")
    longitudc2_var.set(f"{random.uniform(-180, 180):.2f}")
    distanciac2_var.set(f"{random.randint(1, 100)}")
    
    latitud_var.set(f"{random.uniform(-90, 90):.2f}")
    longitud_var.set(f"{random.uniform(-180, 180):.2f}")
    
    eje_x_var.set(f"{random.randint(-100, 100)}")
    eje_y_var.set(f"{random.randint(-100, 100)}")
    eje_z_var.set(f"{random.randint(-100, 100)}")
    
    angulo_carga_var.set(f"{random.randint(0, 180)}")

    # Programar la próxima actualización en 6 segundos (6000 milisegundos)
    ventana.after(6000, actualizar_labels)


# Inicialización de la ventana de Tkinter
ventana = tk.Tk()
ventana.title("Control satelital")
# Ajustar la ventana a pantalla completa
est.pantalla_completa(ventana) 

# Ajustar la ventana a las dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Cargar y establecer la imagen de fondo
ruta_imagen = "Satelite/assets/temple-kukulkan.jpeg"
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

# Creación de la gráfica de presión
canvas_figura_presion, ani_presion = gr.crear_grafica(canvas, posiciones[0], nombres_graficas[0], gr.generador_datos_fake, max_x=5, max_y=100)
animaciones.append(ani_presion)

# Creación de la gráfica de temperatura
canvas_figura_temperatura, ani_temperatura = gr.crear_grafica(canvas, posiciones[1], nombres_graficas[1], gr.generador_datos_fake, max_x=5, max_y=max_y)
animaciones.append(ani_temperatura)

# Creación de la gráfica de velocidad
canvas_figura_velocidad, ani_velocidad = gr.crear_grafica(canvas, posiciones[2], nombres_graficas[2], gr.generador_datos_fake, max_x=5, max_y=max_y)
animaciones.append(ani_velocidad)

# Creación de la gráfica de aceleración
canvas_figura_aceleracion, ani_aceleracion = gr.crear_grafica(canvas, posiciones[3], nombres_graficas[3], gr.generador_datos_fake, max_x=5, max_y=max_y)
animaciones.append(ani_aceleracion)

# Añadir texto al rectángulo blanco

# Crear StringVars para los datos
tiempo_var = tk.StringVar(value=0.0)
altura_var = tk.StringVar(value="XX")

latitudc2_var = tk.StringVar(value="XX")
longitudc2_var = tk.StringVar(value="XX")
distanciac2_var = tk.StringVar(value="XX")


latitud_var = tk.StringVar(value="XX")
longitud_var = tk.StringVar(value="XX")

eje_x_var = tk.StringVar(value="XX")
eje_y_var = tk.StringVar(value="XX")
eje_z_var = tk.StringVar(value="XX")

angulo_carga_var = tk.StringVar(value="XX")

# Colocar las etiquetas y los datos en el canvas
label_tiempo = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 60, "Tiempo:", tiempo_var, "Min")
label_altura = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 120, "Altura:", altura_var, "m")

label_carga_secundaria = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 100, 210-30, "Carga secundaria:", None, None, True)

label_latitud = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 240-30, "Latitud:", latitudc2_var)
label_longitud = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 270-30, "Longitud:", longitudc2_var)
label_distancia = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 300-30, "Distancia respecto C1:", distanciac2_var)

label_orientacion = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 330, "Orientación Carga Primaria:", None, None, True)
label_latitud = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 360, "Latitud:", latitud_var)
label_longitud = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 390, "Longitud:", longitud_var)

label_rotacion = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 420, "Rotación:", None, None, True)
label_eje_x = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 450, "Eje X:", eje_x_var)
label_eje_y = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 480, "Eje Y:", eje_y_var)
label_eje_z = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 510, "Eje Z:", eje_z_var)

label_angulo_carga = est.agregar_texto_y_label(canvas, imagen_duplicada.width + 120, 570, "Ángulo Respecto C2:", angulo_carga_var, "°")
# Repite para otros datos según necesites

# Crear logo y título de Ka'an Astra
 # Cargar y mostrar el logo en la parte superior izquierda
ruta_logo = "Satelite/assets/logo.png" 
logo = Image.open(ruta_logo)
logo = logo.resize((90, 90))
foto_logo = ImageTk.PhotoImage(logo)
canvas.create_image(20, 10, anchor="nw", image=foto_logo)  # Ajusta las coordenadas según necesites

    # Cargar y mostrar el titulo en la parte superior izquierda
ruta_titulo = "Satelite/assets/titulo.png" 
titulo = Image.open(ruta_titulo)
foto_titulo = ImageTk.PhotoImage(titulo)
canvas.create_image(150, 10, anchor="nw", image=foto_titulo)  # Ajusta las coordenadas según necesites

# Iniciar el proceso de actualización periódica de las variables de los labels
ventana.after(6000, actualizar_labels)


# Crear títulos con bordes redondeados de todas las gráficas
est.pack_titulos(canvas)

# Crear botones en el lado izquierdo
est.pack_botones(ventana, canvas, 294 , 815, est.inicioRecoleccionDatos, est.exportar_datos, est.finRecoleccionDatos)

est.minimun_size(ventana, 1200, 800 )

ventana.mainloop()
