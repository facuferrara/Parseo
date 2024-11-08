"""
    Módulo principal del compilador de Logo.
"""

import gramatica as g
import ts as TS
from expresiones import *
from instrucciones import *


def procesar_gira_izq(instr, ts):
    print('> GIRA_IZQUIERDA ', resolver_cadena(instr.cad, ts))


def procesar_imprimir(instr, ts):
    print('> ', resolver_cadena(instr.cad, ts))


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
    if isinstance(exp_num, ExpresionBinaria):
        exp1 = resolver_expresion_aritmetica(exp_num.exp1, ts)
        exp2 = resolver_expresion_aritmetica(exp_num.exp2, ts)
        if exp_num.operador == OPERACION_ARITMETICA.MAS:
            return exp1 + exp2
        if exp_num.operador == OPERACION_ARITMETICA.MENOS:
            return exp1 - exp2
        if exp_num.operador == OPERACION_ARITMETICA.POR:
            return exp1 * exp2
        if exp_num.operador == OPERACION_ARITMETICA.DIVIDIDO:
            return exp1 / exp2
    elif isinstance(exp_num, ExpresionNegativo):
        exp = resolver_expresion_aritmetica(exp_num.exp, ts)
        return exp * -1
    elif isinstance(exp_num, ExpresionNumero):
        return exp_num.val
    elif isinstance(exp_num, ExpresionIdentificador):
        return ts.obtener(exp_num.id).valor


def procesar_instrucciones(instrucciones, ts):
    # lista de instrucciones recolectadas
    for instr in instrucciones:
        if isinstance(instr, Imprimir):
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
            print('Error: instrucción no válida')


f = open("./entrada.txt", "r")
input = f.read()

instrucciones = g.parse(input)
ts_global = TS.TablaDeSimbolos()

procesar_instrucciones(instrucciones, ts_global)
