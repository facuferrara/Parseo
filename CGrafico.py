import turtle

# Configuración de la pantalla
pantalla = turtle.Screen()
pantalla.title("Mi Lenguaje Logo")
pantalla.setup(width=600, height=600)

# Crear la tortuga
t = turtle.Turtle()

# Funciones del lenguaje
def avanza(pasos):
    t.forward(pasos)

def gira_izquierda(grados):
    t.left(grados)

def gira_derecha(grados):
    t.right(grados)

def levanta_pluma():
    t.penup()

def baja_pluma():
    t.pendown()

def posiciona(x, y):
    t.goto(x, y)

# Mapeo de comandos a funciones
comandos = {
    "AVANZA": avanza,
    "GIRA_IZQUIERDA": gira_izquierda,
    "GIRA_DERECHA": gira_derecha,
    "LEVANTA_PLUMA": levanta_pluma,
    "BAJA_PLUMA": baja_pluma,
    "POSICIONA": posiciona
}

# Programa fuente en tu lenguaje
programa = """
AVANZA 100
GIRA_IZQUIERDA 90
AVANZA 100
GIRA_IZQUIERDA 90
AVANZA 100
GIRA_IZQUIERDA 90
AVANZA 100
"""

# Interpretar el programa
def interpreta_programa(programa):
    lineas = programa.strip().split('\n')
    for linea in lineas:
        partes = linea.strip().split()
        if len(partes) == 0:
            continue
        comando = partes[0]
        argumentos = list(map(int, partes[1:]))
        if comando in comandos:
            comandos[comando](*argumentos)

# Ejecutar el programa
interpreta_programa(programa)

# Mantener la ventana abierta
turtle.done()
