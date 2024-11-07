"""
    Módulo para el manejo de la tablas de símbolos.
"""
from enum import Enum


class TIPO_DATO(Enum):
    """
    Esta clase representa los tipo de datos admitidos.
    """
    NUMERO = 1


class Simbolo():
    """
    Esta clase representa un símbolo dentro de nuestra tabla de símbolos.
    """

    def __init__(self, id_key, tipo, valor):
        self.id_key = id_key
        self.tipo = tipo
        self.valor = valor


class TablaDeSimbolos():
    """
    Esta clase representa la tabla de símbolos.
    """

    def __init__(self, simbolos=dict()):
        self.simbolos = simbolos

    def agregar(self, simbolo: Simbolo):
        self.simbolos[simbolo.id_key] = simbolo

    def obtener(self, id_key: str) -> Simbolo:
        try:
            return self.simbolos[id_key]
        except Exception as e:
            raise NameError(f"Error: variable {id_key} no definida.") from e

    def actualizar(self, simbolo: Simbolo):
        try:
            self.simbolos[simbolo.id_key] = simbolo
        except Exception as e:
            raise NameError(f"Error: variable {
                            simbolo.id_key} no definida.") from e
