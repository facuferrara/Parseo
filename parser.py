import ply.yacc as yacc
from lexer import tokens  # Importa los tokens desde lexer.py

# Función para construir el parser y pasar las funciones de movimiento
def build_parser(avanzar, girar_izquierda, girar_derecha, levanta_pluma, baja_pluma):
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
                       | GIRA_DERECHA NUMERO
                       | LEVANTA_PLUMA
                       | BAJA_PLUMA'''
        if p[1] == 'AVANZA':
            distancia = p[2]
            p[0] = lambda: avanzar(distancia)
        elif p[1] == 'GIRA_IZQUIERDA':
            grados = p[2]
            p[0] = lambda: girar_izquierda(grados)
        elif p[1] == 'GIRA_DERECHA':
            grados = p[2]
            p[0] = lambda: girar_derecha(grados)
        elif p[1] == 'LEVANTA_PLUMA':
            p[0] = lambda: levanta_pluma()
        elif p[1] == 'BAJA_PLUMA':
            p[0] = lambda: baja_pluma()            

    # Instrucción de repetición
    def p_instruccion_repite(p):
        'instruccion : REPITE NUMERO LBRACKET instrucciones RBRACKET'
        repeticiones = p[2]  # Número de repeticiones
        instrucciones_a_repetir = p[4]  # Lista de acciones
        p[0] = lambda: [accion() for _ in range(repeticiones) for accion in instrucciones_a_repetir]

    # Manejar errores sintácticos
    def p_error(p):
        print(f"Error de sintaxis en '{p.value}'")

    # Construir el parser
    return yacc.yacc()
