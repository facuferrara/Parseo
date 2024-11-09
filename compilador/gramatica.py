"""
    Módulo para la definicion de la gramática.
"""

import ply.yacc as yacc
from compilador.instrucciones import *
from compilador.expresiones import *
import ply.lex as lex

reservadas = {
    'numero': 'NUMERO',
    'imprimir': 'IMPRIMIR',
    'avanzar': 'AVANZAR',
    'retroceder': 'RETROCEDER',
    'girar_izq': 'GIRAR_IZQUIERDA',
    'right': 'GIRAR_DERECHA',
    'setpos': 'SETPOS',
    'while': 'WHILE',
    'repeat': 'REPEAT',
    'if': 'IF',
    'else': 'ELSE'
}

tokens = [
    'CORIZQ',
    'CORDER',
    'PARIZQ',
    'PARDER',
    'IGUAL',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'CONCAT',
    'MENQUE',
    'MAYQUE',
    'IGUALQUE',
    'NIGUALQUE',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'ID'
] + list(reservadas.values())

# Tokens
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_IGUAL = r'='
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVIDIDO = r'/'
t_CONCAT = r'&'
t_MENQUE = r'<'
t_MAYQUE = r'>'
t_IGUALQUE = r'=='
t_NIGUALQUE = r'!='


def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print(f"Float value too large {t.value}.")
        t.value = 0
    return t


def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print(f"Integer value too large {t.value}.")
        t.value = 0
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Check for reserved words
    t.type = reservadas.get(t.value.lower(), 'ID')
    return t


def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # remuevo las comillas
    return t

# Comentario de múltiples líneas /* .. */


def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...


def t_COMENTARIO_SIMPLE(t):
    r'//.*\n'
    t.lexer.lineno += 1


# Caracteres ignorados
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Caracter illegal '%s' en linea %d, columna %d" % (t.value[0],
                                                             t.lexer.lineno, t.lexer.lexpos))
    t.lexer.skip(1)


# Construyendo el analizador léxico
lexer = lex.lex()


# Asociación de operadores y precedencia
precedence = (
    ('left', 'CONCAT'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO'),
    ('right', 'UMENOS'),
)

# Definición de la gramática


# S -> A
# A -> BI
# B -> I
# I -> imprimir | definir | asignar | while | repeat | if | ifelse

def p_init(t):
    'init            : instrucciones'
    t[0] = t[1]


def p_instrucciones_lista(t):
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t):
    'instrucciones    : instruccion '
    t[0] = [t[1]]


def p_instruccion(t):
    '''instruccion      : imprimir_instr
                        | avanzar_instr
                        | girar_izq_instr
                        | girar_der_instr
                        | retroceder_instr
                        | setpos_instr
                        | definicion_instr
                        | asignacion_instr
                        | mientras_instr
                        | repeat_instr
                        | if_instr
                        | if_else_instr'''
    t[0] = t[1]


def p_instruccion_imprimir(t):
    'imprimir_instr     : IMPRIMIR PARIZQ expresion_cadena PARDER'
    t[0] = Imprimir(t[3])


def p_avanzar_instr(t):
    'avanzar_instr     : AVANZAR expresion_numerica'
    t[0] = Avanzar(t[2])

def p_retroceder_instr(t):
    'retroceder_instr  : RETROCEDER expresion_numerica'
    t[0] = Retroceder(t[2])


def p_girar_izq_instr(t):
    'girar_izq_instr     : GIRAR_IZQUIERDA expresion_numerica'
    t[0] = GirarIzquierda(t[2])

def p_girar_der_instr(t):
    'girar_der_instr     : GIRAR_DERECHA expresion_numerica'
    t[0] = GirarDerecha(t[2])

def p_instruccion_definicion(t):
    'definicion_instr   : NUMERO ID'
    t[0] = Definicion(t[2])


def p_asignacion_instr(t):
    'asignacion_instr   : ID IGUAL expresion_numerica'
    t[0] = Asignacion(t[1], t[3])

def p_setpos_instr(t):
    'setpos_instr : SETPOS CORIZQ expresion_numerica expresion_numerica CORDER'
    t[0] = SetPosicion(t[3], t[4])

def p_mientras_instr(t):
    'mientras_instr     : WHILE expresion_logica CORIZQ instrucciones CORDER'
    t[0] = Mientras(t[2], t[4])

def p_repeat_instr(t):
    'repeat_instr       : REPEAT expresion_numerica CORIZQ instrucciones CORDER'
    t[0] = Repeat(t[2], t[4])


def p_if_instr(t):
    'if_instr           : IF expresion_logica CORIZQ instrucciones CORDER'
    t[0] = If(t[2], t[4])


def p_if_else_instr(t):
    'if_else_instr      : IF expresion_logica CORIZQ instrucciones CORDER ELSE CORIZQ instrucciones CORDER'
    t[0] = IfElse(t[2], t[4], t[8])


def p_expresion_binaria(t):
    '''expresion_numerica : expresion_numerica MAS expresion_numerica
                        | expresion_numerica MENOS expresion_numerica
                        | expresion_numerica POR expresion_numerica
                        | expresion_numerica DIVIDIDO expresion_numerica'''
    if t[2] == '+':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MAS)
    elif t[2] == '-':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MENOS)
    elif t[2] == '*':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POR)
    elif t[2] == '/':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.DIVIDIDO)


def p_expresion_unaria(t):
    'expresion_numerica : MENOS expresion_numerica %prec UMENOS'
    t[0] = ExpresionNegativo(t[2])


def p_expresion_agrupacion(t):
    'expresion_numerica : PARIZQ expresion_numerica PARDER'
    t[0] = t[2]


def p_expresion_number(t):
    '''expresion_numerica : ENTERO
                        | DECIMAL'''
    t[0] = ExpresionNumero(t[1])


def p_expresion_id(t):
    'expresion_numerica   : ID'
    t[0] = ExpresionIdentificador(t[1])


def p_expresion_concatenacion(t):
    'expresion_cadena     : expresion_cadena CONCAT expresion_cadena'
    t[0] = ExpresionConcatenar(t[1], t[3])


def p_expresion_cadena(t):
    'expresion_cadena     : CADENA'
    t[0] = ExpresionDobleComilla(t[1])


def p_expresion_cadena_numerico(t):
    'expresion_cadena     : expresion_numerica'
    t[0] = ExpresionCadenaNumerico(t[1])


def p_expresion_logica(t):
    '''expresion_logica : expresion_numerica MAYQUE expresion_numerica
                        | expresion_numerica MENQUE expresion_numerica
                        | expresion_numerica IGUALQUE expresion_numerica
                        | expresion_numerica NIGUALQUE expresion_numerica'''
    if t[2] == '>':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MAYOR_QUE)
    elif t[2] == '<':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MENOR_QUE)
    elif t[2] == '==':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.IGUAL)
    elif t[2] == '!=':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.DIFERENTE)


def p_error(t):
    print(t)
    print(f"Error sintáctico en '{t.value}'.")


parser = yacc.yacc(debug=False, write_tables=False)

def parse(input):
    return parser.parse(input)
