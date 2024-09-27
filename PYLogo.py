import ply.lex as lex
import ply.yacc as yacc

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
    if p[1] == 'AVANZA':
        p[0] = f't.forward({p[2]})'
    elif p[1] == 'GIRA_IZQUIERDA':
        p[0] = f't.left({p[2]})'
    elif p[1] == 'GIRA_DERECHA':
        p[0] = f't.right({p[2]})'

# Instrucción de repetición
def p_instruccion_repite(p):
    'instruccion : REPITE NUMERO LBRACKET instrucciones RBRACKET'
    p[0] = f'for _ in range({p[2]}):\n    ' + '\n    '.join(p[4])

# Manejar errores sintácticos
def p_error(p):
    print(f"Error de sintaxis en '{p.value}'")

# Construir el parser
parser = yacc.yacc()

# ---------------------------
# PROBAR EL PARSER
# ---------------------------

# Ejemplo de código de prueba
codigo = '''
AVANZA 100
GIRA_IZQUIERDA 90
REPITE 4 [
    AVANZA 50
    GIRA_DERECHA 90
]
'''

# Analizar el código
resultado = parser.parse(codigo)
print("\n".join(resultado))

# Puedes ahora ejecutar este código y ver cómo se generan las instrucciones Python.
