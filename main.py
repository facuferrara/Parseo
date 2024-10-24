import tkinter as tk
from parser import build_parser  # Importa la función que construye el parser
from lexer import lexer  # Importa el lexer desde lexer.py
from math import cos, sin, radians

# Inicializar la ventana y el canvas de Tkinter
root = tk.Tk()
root.title("Intérprete Tortuga")

canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack()

# Variables para la posición inicial de la tortuga
x, y = 250, 250  # Centro del canvas
angle = 0  # Ángulo inicial (0 grados, hacia la derecha)
lapiz_abajo = True  # Controla si la tortuga está dibujando o no

# Funciones para el dibujo
def avanzar(distancia):
    global x, y, angle, lapiz_abajo
    new_x = x + distancia * cos(radians(angle))
    new_y = y - distancia * sin(radians(angle))
    if lapiz_abajo:
        canvas.create_line(x, y, new_x, new_y)
    x, y = new_x, new_y

def girar_izquierda(grados):
    global angle
    angle = (angle + grados) % 360

def girar_derecha(grados):
    global angle
    angle = (angle - grados) % 360

# Construir el parser con las funciones de movimiento
parser = build_parser(avanzar, girar_izquierda, girar_derecha)

# Ejemplo de código de prueba
codigo = '''
AVANZA 100
GIRA_IZQUIERDA 90
REPITE 4 [
    AVANZA 50
    GIRA_DERECHA 90
]
'''

# Utiliza el lexer y el parser para procesar el código
resultado = parser.parse(codigo, lexer=lexer)

# Ejecuta las acciones generadas por el parser
for accion in resultado:
    accion()

# Ejecutar el bucle principal de la ventana Tkinter
root.mainloop()
