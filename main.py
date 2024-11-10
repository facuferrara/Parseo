"""
    Módulo principal del compilador de Logo.
"""

import argparse
import time
import tkinter as tk

from math import cos, sin, radians

import compilador.gramatica as gram
import compilador.ts as TS
from compilador.instrucciones import *
from compilador.expresiones import *

# Inicializar la ventana y el canvas de Tkinter
root = tk.Tk()
root.title("Intérprete Tortuga")

canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack()

# Variables para la posición inicial de la tortuga
# Centro del canvas
x, y = 250, 250
y_text = 10

# Ángulo inicial (0 grados, hacia la derecha)
angle = 0

# Controla si la tortuga está dibujando o no
lapiz_abajo = True

# Funciones para el dibujo


def avanzar(distancia):
    global x, y, angle, lapiz_abajo
    new_x = x + distancia * cos(radians(angle))
    new_y = y - distancia * sin(radians(angle))
    if lapiz_abajo:
        time.sleep(0.7)
        canvas.create_line(x, y, new_x, new_y)
        canvas.update()
    x, y = new_x, new_y
    # Actualizacion grafica para el show
    # canvas.create_text(x, y, text=f"({x}, {y})", fill="black", font=("Helvetica", 8))
     
def retroceder(distancia):
    global x, y, angle, lapiz_abajo
    new_x = x - distancia * cos(radians(angle))
    new_y = y + distancia * sin(radians(angle))
    if lapiz_abajo:
        time.sleep(0.7)
        canvas.create_line(x, y, new_x, new_y)
        canvas.update()
    x, y = new_x, new_y
    
def setpos(x_new, y_new):
    global x, y
    x, y = x_new, y_new  # Actualiza la posición de la tortuga sin dibujar


def girar_izquierda(grados):
    global angle
    angle = (angle + grados) % 360


def girar_derecha(grados):
    global angle
    angle = (angle - grados) % 360


def actualizar_pluma(estado):
    global lapiz_abajo
    lapiz_abajo = estado

def imprimir_tk(cadena):
    global y_text
    textID = canvas.create_text(240,y_text, justify='left', text=cadena)
    canvas.update()
    y_text+=10


def clean():
    canvas.delete("all")


def home():
    setpos(250, 250)


def clear_screen():
    clean()
    home()

# Funciones para el procesamiento de las instrucciones
def procesar_avanzar(instr, ts):
    val = resolver_expresion_aritmetica(instr.exp_numerica, ts)
    print('> AVANZAR ', val)
    avanzar(val)

def procesar_retroceder(instr, ts):
    val = resolver_expresion_aritmetica(instr.exp_numerica, ts)
    print('> RETROCEDER ', val)
    retroceder(val)

def procesar_gira_izq(instr, ts):
    val = resolver_expresion_aritmetica(instr.exp_numerica, ts)
    print('> GIRA_IZQUIERDA ', val)
    girar_izquierda(val)

def procesar_gira_der(instr, ts):
    val = resolver_expresion_aritmetica(instr.exp_numerica, ts)
    print('> GIRA_DERECHA ', val)
    girar_derecha(val)

def procesar_imprimir(instr, ts):
    val = resolver_cadena(instr.cad, ts)
    print('> ', val)
    imprimir_tk(val)

def procesar_setpos(instr, ts):
    val_x = resolver_expresion_aritmetica(instr.exp_x, ts)
    val_y = resolver_expresion_aritmetica(instr.exp_y, ts)
    print(f'> SETPOS a ({val_x}, {val_y})')
    setpos(val_x, val_y)

def procesar_pen(instr, ts):
    actualizar_pluma(instr.state)


def procesar_home(instr, ts):
    home()

def procesar_clean(instr, ts):
    clean()

def procesar_clear_screen(instr, ts):
    clear_screen()

def procesar_definicion(instr, ts):
    # inicializamos con 0 como valor por defecto
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, 0)
    ts.agregar(simbolo)


def procesar_asignacion(instr, ts):
    val = resolver_expresion_aritmetica(instr.exp_numerica, ts)
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, val)
    ts.actualizar(simbolo)


def procesar_mientras(instr, ts):
    while resolver_expresion_logica(instr.exp_logica, ts):
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrucciones, ts_local)


def procesar_repeat(instr, ts):
    val = resolver_expresion_aritmetica(instr.exp_numerica, ts)
    for _ in range(int(val)):
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrucciones, ts_local)


def procesar_if(instr, ts):
    val = resolver_expresion_logica(instr.exp_logica, ts)
    if val:
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrucciones, ts_local)


def procesar_if_else(instr, ts):
    val = resolver_expresion_logica(instr.exp_logica, ts)
    if val:
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instr_if_verdadero, ts_local)
    else:
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instr_if_falso, ts_local)


def resolver_cadena(expCad, ts):
    if isinstance(expCad, ExpresionConcatenar):
        exp1 = resolver_cadena(expCad.exp1, ts)
        exp2 = resolver_cadena(expCad.exp2, ts)
        return exp1 + exp2
    elif isinstance(expCad, ExpresionDobleComilla):
        return expCad.val
    elif isinstance(expCad, ExpresionCadenaNumerico):
        return str(resolver_expresion_aritmetica(expCad.exp, ts))
    else:
        print('Error: Expresión cadena no válida')


def resolver_expresion_logica(exp_log, ts):
    exp1 = resolver_expresion_aritmetica(exp_log.exp1, ts)
    exp2 = resolver_expresion_aritmetica(exp_log.exp2, ts)
    if exp_log.operador == OPERACION_LOGICA.MAYOR_QUE:
        return exp1 > exp2
    if exp_log.operador == OPERACION_LOGICA.MENOR_QUE:
        return exp1 < exp2
    if exp_log.operador == OPERACION_LOGICA.IGUAL:
        return exp1 == exp2
    if exp_log.operador == OPERACION_LOGICA.DIFERENTE:
        return exp1 != exp2


def resolver_expresion_aritmetica(exp_num, ts):
    """
    Resuelve una expresión aritmética, que puede ser una expresión binaria,
    una variable (identificador), un número literal o una expresión negativa.
    """
    # Si es una expresión binaria (por ejemplo, a + b)
    if isinstance(exp_num, ExpresionBinaria):
        # Resolver las dos expresiones involucradas
        exp1 = resolver_expresion_aritmetica(exp_num.exp1, ts)
        exp2 = resolver_expresion_aritmetica(exp_num.exp2, ts)
        
        # Dependiendo del operador, realizamos la operación correspondiente
        if exp_num.operador == OPERACION_ARITMETICA.MAS:
            return exp1 + exp2
        elif exp_num.operador == OPERACION_ARITMETICA.MENOS:
            return exp1 - exp2
        elif exp_num.operador == OPERACION_ARITMETICA.POR:
            return exp1 * exp2
        elif exp_num.operador == OPERACION_ARITMETICA.DIVIDIDO:
            return exp1 / exp2
    
    # Si es una expresión de negativo (por ejemplo, -a)
    elif isinstance(exp_num, ExpresionNegativo):
        # Resolver la expresión y devolver el valor negativo
        exp = resolver_expresion_aritmetica(exp_num.exp, ts)
        return exp * -1
    
    # Si es un número literal (por ejemplo, 10)
    elif isinstance(exp_num, ExpresionNumero):
        return exp_num.val
    
    # Si es un identificador (por ejemplo, una variable como 'distancia')
    elif isinstance(exp_num, ExpresionIdentificador):
        # Obtener el símbolo de la tabla de símbolos y devolver su valor
        simbolo = ts.obtener(exp_num.id)
        return simbolo.valor
    
    # Si no es ninguno de los tipos anteriores, se lanza un error
    else:
        raise TypeError(f"Tipo de expresión no soportado: {type(exp_num)}")


def procesar_instrucciones(instrucciones, ts):
    # lista de instrucciones recolectadas
    for instr in instrucciones:
        
        if isinstance(instr, Avanzar):
            procesar_avanzar(instr, ts)
        elif isinstance(instr, SetPosicion):
            procesar_setpos(instr, ts)          
        elif isinstance(instr, SetPen):
            procesar_pen(instr, ts)
        elif isinstance(instr, Home):
            procesar_home(instr, ts)
        elif isinstance(instr, Clean):
            procesar_clean(instr, ts)
        elif isinstance(instr, ClearScreen):
            procesar_clear_screen(instr, ts)
        elif isinstance(instr, Retroceder):
            procesar_retroceder(instr, ts)
        elif isinstance(instr, GirarIzquierda):
            procesar_gira_izq(instr, ts)
        elif isinstance(instr, GirarDerecha):
            procesar_gira_der(instr, ts)
        elif isinstance(instr, Imprimir):
            procesar_imprimir(instr, ts)
        elif isinstance(instr, Definicion):
            procesar_definicion(instr, ts)
        elif isinstance(instr, Asignacion):
            procesar_asignacion(instr, ts)
        elif isinstance(instr, Mientras):
            procesar_mientras(instr, ts)
        elif isinstance(instr, Repeat):
            procesar_repeat(instr, ts)
        elif isinstance(instr, If):
            procesar_if(instr, ts)
        elif isinstance(instr, IfElse):
            procesar_if_else(instr, ts)
        else:
            # print('Error: instrucción no válida')
            print(f"Instrucción no reconocida: {instr_type}")
            break


# Parseo de la linea de comando para la utilizacion del script

cli = argparse.ArgumentParser(description='Un simple compilador de Logo.')
cli.add_argument("-f", "--file", help="Nombre de archivo a procesar")

args = cli.parse_args()

codigo = ""

if args.file:
    try:
        with open(args.file, encoding="utf8") as file:
            codigo = file.read()
    except IOError as e:
        print(f"Archivo no encontrado: '{args.file}'")

if codigo:
    # Utiliza el lexer y el parser para procesar el código
    instrucciones = gram.parse(codigo)
    ts_global = TS.TablaDeSimbolos()

    procesar_instrucciones(instrucciones, ts_global)

    # Ejecutar el bucle principal de la ventana Tkinter
    root.mainloop()

