import ply.lex as lex

# Definir los tokens
tokens = (
    'AVANZA',
    'GIRA_IZQUIERDA',
    'GIRA_DERECHA',
    'REPITE',
    'SI',
    'NUMERO',
    'LBRACKET',  # [
    'RBRACKET',  # ]
    'LEVANTA_PLUMA',
    'BAJA_PLUMA'
)

# Expresiones regulares para cada token
t_AVANZA = r'AVANZA'
t_GIRA_IZQUIERDA = r'GIRA_IZQUIERDA'
t_GIRA_DERECHA = r'GIRA_DERECHA'
t_REPITE = r'REPITE'
t_SI = r'SI'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LEVANTA_PLUMA = r'LEVANTA_PLUMA'
t_BAJA_PLUMA = r'BAJA_PLUMA'

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

# Manejar comentarios (opcional)
def t_COMENTARIO(t):
    r'\#.*'
    pass

# Construir el lexer
lexer = lex.lex()
