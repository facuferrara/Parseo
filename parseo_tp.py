import turtle

# Configuración de la pantalla
pantalla = turtle.Screen()
pantalla.title("Mi Lenguaje Logo")
pantalla.setup(width=600, height=600)

# Crear la tortuga
t = turtle.Turtle()

# Programa fuente: Dibuja un cuadrado
programa_cuadrado = [
    "AVANZA 100",
    "GIRA_IZQUIERDA 90",
    "AVANZA 100",
    "GIRA_IZQUIERDA 90",
    "AVANZA 100",
    "GIRA_IZQUIERDA 90",
    "AVANZA 100"
]

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

# Interpretar el programa
def interpreta(comando):
    partes = comando.strip().split()
    instruccion = partes[0]

    if instruccion == "AVANZA":
        avanza(int(partes[1]))
    elif instruccion == "GIRA_IZQUIERDA":
        gira_izquierda(int(partes[1]))
    elif instruccion == "GIRA_DERECHA":
        gira_derecha(int(partes[1]))
    elif instruccion == "LEVANTA_PLUMA":
        levanta_pluma()
    elif instruccion == "BAJA_PLUMA":
        baja_pluma()
    elif instruccion == "POSICIONA":
        posiciona(int(partes[1]), int(partes[2]))

# Ejecutar el programa
for comando in programa_cuadrado:
    interpreta(comando)

# Mantener la ventana abierta
turtle.done()
