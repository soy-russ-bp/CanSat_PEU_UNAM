import tkinter as tk
from PIL import Image, ImageTk

"""def agregar_texto_y_label(canvas, x, y, texto, nombre_variable):
    # Crear y colocar el texto estático
    canvas.create_text(x, y, text=texto, fill="black", font=("Arial", 14)) 
    # Crear el Label para los datos dinámicos
    variable_label = tk.Label(canvas, textvariable=nombre_variable, bg="white", font=("Arial", 14), fg="black" )
    variable_window = canvas.create_window(x + 100, y, window=variable_label, anchor="w")
    return variable_label"""

def agregar_texto_y_label(canvas, x, y, texto, nombre_variable, negritas=False):
    # Determinar el estilo de la fuente según si se quiere en negritas o no
    estilo_fuente = "Arial 14 bold" if negritas else "Arial 14"
    
    # Crear y colocar el texto estático
    canvas.create_text(x, y, text=texto, fill="black", font=estilo_fuente) 
    
    # Crear el Label para los datos dinámicos
    variable_label = tk.Label(canvas, textvariable=nombre_variable, bg="white", font=estilo_fuente, fg="black" )
    variable_window = canvas.create_window(x + 100, y, window=variable_label, anchor="w")
    
    return variable_label

def crear_titulo_borde_redondeado(canvas, x1, y1, x2, y2, texto, radio=10, ancho_borde=2, color_borde="yellow", color_fondo="yellow", color_texto="black"):
    # Dibujar las esquinas redondeadas
    canvas.create_arc(x1, y1, x1 + 2*radio, y1 + 2*radio, start=90, extent=90, fill=color_fondo, outline=color_borde, width=ancho_borde)
    canvas.create_arc(x2 - 2*radio, y1, x2, y1 + 2*radio, start=0, extent=90, fill=color_fondo, outline=color_borde, width=ancho_borde)
    canvas.create_arc(x1, y2 - 2*radio, x1 + 2*radio, y2, start=180, extent=90, fill=color_fondo, outline=color_borde, width=ancho_borde)
    canvas.create_arc(x2 - 2*radio, y2 - 2*radio, x2, y2, start=270, extent=90, fill=color_fondo, outline=color_borde, width=ancho_borde)

    # Dibujar los lados del rectángulo
    canvas.create_rectangle(x1 + radio, y1, x2 - radio, y2, fill=color_fondo, outline=color_borde, width=ancho_borde)
    canvas.create_rectangle(x1, y1 + radio, x2, y2 - radio, fill=color_fondo, outline=color_borde, width=ancho_borde)

    # Añadir texto al rectángulo en negritas
    canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=texto, fill=color_texto, font=("Arial", 14, "bold"), anchor="center")

def pantalla_completa(ventana):
    ventana.attributes("-fullscreen", True)
    
def minimun_size(ventana, width, height):
    ventana.update_idletasks()
    ventana.minsize(width, height)
    
def pack_titulos(canvas):
    crear_titulo_borde_redondeado(canvas, 50, 110, 450, 160, "Presión")
    crear_titulo_borde_redondeado(canvas, 520, 110, 920, 160, "Temperatra")
    crear_titulo_borde_redondeado(canvas, 50, 470, 450, 520, "Velocidad")
    crear_titulo_borde_redondeado(canvas, 520, 470, 920, 520, "Aceleración")
    

   
def inicioRecoleccionDatos():
    print("Inicio de recolección de datos")
def exportar_datos():
    print("Exportando datos")
def finRecoleccionDatos():
    print("Fin de recolección de datos")
    
# Crear un Frame como contenedor de los botones
def pack_botones(ventana, canvas, x, y, inicioRecoleccionDatos, exportar_datos, finRecoleccionDatos):
    frame_botones = tk.Frame(ventana)
    frame_botones.pack(side="left", fill="y")
        
    boton_inicio = tk.Button(frame_botones, text="Inicio", bg="purple", fg="black", width=10, height=1, command=inicioRecoleccionDatos)
    boton_inicio.pack(side="left", fill="x")  # Ahora usamos 'top' para el orden dentro del Frame

    boton_export_data = tk.Button(frame_botones, text="Export data", bg="purple", fg="black", width=10, height=1, command=exportar_datos)
    boton_export_data.pack(side="left", fill="x")

        
    boton_fin_recoleccion = tk.Button(frame_botones, text="Fin", bg="purple", fg="black", width=10, height=1, command=finRecoleccionDatos)
    boton_fin_recoleccion.pack(side="left", fill="x")

    # Colocar el Frame de los botones en el canvas
    canvas.create_window(x, y, window=frame_botones, anchor="nw") # Ajusta la posición según necesites