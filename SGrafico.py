#Definir Tokens, para identificar cada palabra del programa.


# Tamaño de la cuadrícula (puedes cambiar el tamaño según tus necesidades)
grid_size = 20

# Crear una cuadrícula vacía
grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

# Posición inicial de la tortuga en el centro de la cuadrícula
x, y = grid_size // 2, grid_size // 2

# Dirección inicial de la tortuga (0: arriba, 1: derecha, 2: abajo, 3: izquierda)
direccion = 1

# Pluma levantada o bajada
pluma_abajo = True

# Funciones del lenguaje
def avanza(pasos):
    global x, y
    for _ in range(pasos):
        if direccion == 0:  # Arriba
            y = max(0, y - 1)
        elif direccion == 1:  # Derecha
            x = min(grid_size - 1, x + 1)
        elif direccion == 2:  # Abajo
            y = min(grid_size - 1, y + 1)
        elif direccion == 3:  # Izquierda
            x = max(0, x - 1)
        
        if pluma_abajo:
            grid[y][x] = '*'

def gira_izquierda(grados):
    global direccion
    pasos = grados // 90
    direccion = (direccion - pasos) % 4

def gira_derecha(grados):
    global direccion
    pasos = grados // 90
    direccion = (direccion + pasos) % 4

def levanta_pluma():
    global pluma_abajo
    pluma_abajo = False

def baja_pluma():
    global pluma_abajo
    pluma_abajo = True

def posiciona(nx, ny):
    global x, y
    x, y = nx, ny
    if pluma_abajo:
        grid[y][x] = '*'

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

# Programa fuente: Dibuja un cuadrado
programa_cuadrado = [
    "AVANZA 4",
    "GIRA_IZQUIERDA 90",
    "AVANZA 4",
    "GIRA_IZQUIERDA 90",
    "AVANZA 4",
    "GIRA_IZQUIERDA 90",
    "AVANZA 4"
]
# Programa fuente: Dibuja una "L"
programa_L = [
    "AVANZA 4",          # Avanza hacia adelante
    "GIRA_IZQUIERDA 90", # Gira a la izquierda 90 grados
    "AVANZA 2"           # Avanza hacia arriba o abajo (dependiendo de la orientación inicial)
]

# Ejecutar el programa para dibujar la "L"
for comando in programa_L:
    interpreta(comando)

# Ejecutar el programa
#for comando in programa_cuadrado:
#    interpreta(comando)

# Imprimir la cuadrícula
for fila in grid:
    print(' '.join(fila))
