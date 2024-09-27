import ply.lex as lex
import ply.yacc as yacc
import tkinter as tk
from math import cos, sin, radians

# ---------------------------
# PARTE LÉXICA
# ---------------------------

# Definir los tokens
tokens = (
    'AVANZA',
    'GIRA_IZQUIERDA',
    'GIRA_DERECHA',
    'REPITE',
    'NUMERO',
    'LBRACKET',  # [
    'RBRACKET'   # ]
)

# Definir las expresiones regulares para cada token
t_AVANZA = r'AVANZA'
t_GIRA_IZQUIERDA = r'GIRA_IZQUIERDA'
t_GIRA_DERECHA = r'GIRA_DERECHA'
t_REPITE = r'REPITE'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

# Definir el token para números
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)  # Convertir a entero
    return t

# Ignorar espacios y saltos de línea
t_ignore = ' \t\n'

# Manejar errores léxicos
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# ---------------------------
# PARTE SINTÁCTICA
# ---------------------------

# Inicializar posición y dirección de la tortuga
x, y = 250, 250  # Posición inicial
angle = 0  # Ángulo inicial (hacia la derecha)

# Lista para almacenar las acciones generadas
actions = []

# Definir las reglas gramaticales

# Instrucciones (secuencia de instrucciones)
def p_instrucciones(p):
    '''instrucciones : instruccion
                     | instrucciones instruccion'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

# Instrucción: AVANZA, GIRA_IZQUIERDA, GIRA_DERECHA
def p_instruccion(p):
    '''instruccion : AVANZA NUMERO
                   | GIRA_IZQUIERDA NUMERO
                   | GIRA_DERECHA NUMERO'''
    global angle
    if p[1] == 'AVANZA':
        distance = p[2]
        p[0] = lambda: avanzar(distance)
    elif p[1] == 'GIRA_IZQUIERDA':
        grados = p[2]
        p[0] = lambda: girar_izquierda(grados)
    elif p[1] == 'GIRA_DERECHA':
        grados = p[2]
        p[0] = lambda: girar_derecha(grados)

# Instrucción de repetición
def p_instruccion_repite(p):
    'instruccion : REPITE NUMERO LBRACKET instrucciones RBRACKET'
    repeticiones = p[2]  # Esto debe ser un número entero
    instrucciones_a_repetir = p[4]  # Esto es una lista de funciones
    p[0] = lambda: [accion() for _ in range(repeticiones) for accion in instrucciones_a_repetir]

# Manejar errores sintácticos
def p_error(p):
    print(f"Error de sintaxis en '{p.value}'")

# Construir el parser
parser = yacc.yacc()

# ---------------------------
# FUNCIONES PARA EL DIBUJO
# ---------------------------

# Función para avanzar en la dirección actual
def avanzar(distancia):
    global x, y, angle
    new_x = x + distancia * cos(radians(angle))
    new_y = y - distancia * sin(radians(angle))
    canvas.create_line(x, y, new_x, new_y)
    x, y = new_x, new_y

# Función para girar a la izquierda
def girar_izquierda(grados):
    global angle
    angle = (angle + grados) % 360

# Función para girar a la derecha
def girar_derecha(grados):
    global angle
    angle = (angle - grados) % 360

# ---------------------------
# PROGRAMA PRINCIPAL
# ---------------------------

# Inicializar la ventana y el canvas de Tkinter
root = tk.Tk()
root.title("Intérprete Tortuga")

canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack()

# Ejemplo de código de prueba
codigo = '''
AVANZA 100
GIRA_IZQUIERDA 90
REPITE 4 [
    AVANZA 50
    GIRA_DERECHA 90
]
'''

# Analizar el código e interpretar las instrucciones
resultado = parser.parse(codigo)
for accion in resultado:
    accion()

# Ejecutar el bucle principal de la ventana Tkinter
root.mainloop()
