"""
    Módulo para el manejo de la instrucciones.
"""


class Instruccion:
    """
    Clase abstracta de instruciones.
    """


class Imprimir(Instruccion):
    """
        Esta clase representa la instrucción imprimir.
        La instrucción imprimir únicamente tiene como parámetro una cadena
    """

    def __init__(self,  cad):
        self.cad = cad


class Avanzar(Instruccion):
    """
        Esta clase representa la instrucción avanzar.
        La instrucción girar izquierda únicamente tiene como parámetro los grados.
    """

    def __init__(self,  exp_numerica):
        self.exp_numerica = exp_numerica


class GirarIzquierda(Instruccion):
    """
        Esta clase representa la instrucción girar izquierda.
        La instrucción girar izquierda únicamente tiene como parámetro los grados.
    """

    def __init__(self,  exp_numerica):
        self.exp_numerica = exp_numerica


class Mientras(Instruccion):
    """
        Esta clase representa la instrucción mientras.
        La instrucción mientras recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    """

    def __init__(self, exp_logica, instrucciones=None):
        self.exp_logica = exp_logica
        self.instrucciones = [] if instrucciones is None else instrucciones


class Repeat(Instruccion):
    """
        Esta clase representa la instrucción repeat.
        La instrucción repeat recibe como parámetro una expresión numerica y la lista
        de instrucciones a ejecutar esa cantidad de veces.
    """

    def __init__(self, exp_numerica, instrucciones=None):
        self.exp_numerica = exp_numerica
        self.instrucciones = [] if instrucciones is None else instrucciones


class Definicion(Instruccion):
    """
        Esta clase representa la instrucción de definición de variables.
        Recibe como parámetro el nombre del identificador a definir
    """

    def __init__(self, id):
        self.id = id


class Asignacion(Instruccion):
    """
        Esta clase representa la instrucción de asignación de variables
        Recibe como parámetro el identificador a asignar y el valor que será asignado.
    """

    def __init__(self, id, exp_numerica):
        self.id = id
        self.exp_numerica = exp_numerica


class If(Instruccion):
    """
        Esta clase representa la instrucción if.
        La instrucción if recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    """

    def __init__(self, exp_logica, instrucciones=None):
        self.exp_logica = exp_logica
        self.instrucciones = [] if instrucciones is None else instrucciones


class IfElse(Instruccion):
    """
        Esta clase representa la instrucción if-else.
        La instrucción if-else recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera y otro lista de 
        instrucciones a ejecutar si la expresión lógica es falsa.
    """

    def __init__(self, exp_logica, instr_if_verdadero=None, instr_if_falso=None):
        self.exp_logica = exp_logica
        self.instr_if_verdadero = [] if instr_if_verdadero is None else instr_if_verdadero
        self.instr_if_falso = [] if instr_if_falso is None else instr_if_falso
