# Parseo y Generación de Código

## Trabajo Práctico

**Profesor:** Mag. Ing. Pablo Pandolfo

**Alumnos:**
- Ferrara Facundo Matias
- Origlia Pablo Daniel

**Año:** 2024

---

## Índice

- [Parseo y Generación de Código](#parseo-y-generación-de-código)
  - [Trabajo Práctico](#trabajo-práctico)
  - [Índice](#índice)
  - [Objetivo](#objetivo)
  - [Descripción](#descripción)
  - [Repositorio](#repositorio)
  - [Definición del Lenguaje](#definición-del-lenguaje)
  - [Implementación](#implementación)
    - [Scanner](#scanner)
    - [Parser](#parser)
    - [Tabla de símbolos](#tabla-de-símbolos)
    - [Main (main.py)](#main-mainpy)
    - [Acciones Semánticas](#acciones-semánticas)
  - [Casos de Prueba Automatizados](#casos-de-prueba-automatizados)
  - [Conclusiones](#conclusiones)
  - [Versión PYLogo](#versión-pylogo)
  - [Acciones disponibles](#acciones-disponibles)
  - [Ejemplo de programa](#ejemplo-de-programa)

---

## Objetivo

Diseñar y desarrollar un compilador de una versión reducida del lenguaje de programación inspirado en LOGO, utilizando las herramientas de análisis léxico y sintáctico proporcionadas por PLY (Python Lex-Yacc).

## Descripción

El lenguaje PYLogo está inspirado en LOGO y está diseñado para enseñar conceptos básicos de programación y control de movimiento gráfico en una interfaz simple. Permite a los usuarios controlar una "tortuga" que dibuja gráficos mediante comandos como avanzar, girar y levantar o bajar el lápiz. El lenguaje es fácil de entender y sigue un enfoque basado en acciones que dirigen el comportamiento de la tortuga en un plano de coordenadas.

## Repositorio

1. Clonar el Proyecto  
   Primero, asegúrate de tener git instalado. Si no lo tienes, puedes instalarlo siguiendo las instrucciones de git-scm.com.  
   Luego, para clonar un repositorio de GitHub (o cualquier otro repositorio Git), ejecuta el siguiente comando en tu terminal:
  
  ```bash
  git clone https://github.com/facuferrara/Parseo.git
  ```

2. Navegar al Directorio del Proyecto  
Después de clonar el proyecto, entra en el directorio del proyecto con el siguiente comando:

```bash
cd Parseo
```
3. Activar el entorno virtual
Para poder correr la aplicacion en un entorno que no afecte los modulos instalados en la computadora local y evitar conflicto con las versiones de los diferentes modulos utilizados, se hace uso de un entorno virtual, para activarlo:

```bash
.venv\Scripts\Activate.ps1
```

3. Instalar Dependencias  
El proyecto utiliza Python y tiene un archivo `requirements.txt`, puedes instalar las dependencias con:

```bash
pip install -r requirements.txt
```

4. Ejecutar el Programa  
Una vez todo esté en su lugar, puedes ejecutar el programa con el modificador `-f` o `--file` seguido del nombre del archivo a ejecutar:

```bash
python.exe main.py -f FILENAME
```

## Definición del Lenguaje

PYLogo es un lenguaje de programación basado en comandos simples que permite a los usuarios interactuar con una "tortuga" para crear gráficos en un plano de coordenadas.

## Implementación

### Scanner

Se ha implementado un scanner que analiza el código fuente de PYLogo, identificando los diferentes tokens que se utilizan en el lenguaje. Para esto en el modulo `gramatica.py` se definen los diferentes tokens que componen el lenguaje, como comandos e identificadores, utilizando la biblioteca `PLY` para crear un lexer que identifica y clasifica los elementos del código fuente. El lexer ignora espacios, comentarios y saltos de línea, y genera errores para caracteres no válidos.

### Parser

El parser se encarga de analizar la estructura del código PYLogo, validando que los comandos sigan la gramática definida. Es responsable del análisis sintáctico del lenguaje PYLogo. Utiliza el módulo `gramatica.py` donde está definida la misma y la creación del parser, además cada instrucción esta definida como clase en el módulo `instrucciones.py` adicionalmente dentro del módulo `expresiones.py` se definen las expresiones en forma de clases para ser procesadas por el parse junto con las instrucciones para generar la ejecución del programa fuente dentro de una ventana de `Tkinter`, validando que los comandos en el código fuente cumplan con las reglas sintácticas y semanticas. El parser organiza las estructuras de los comandos y controla la correcta jerarquía de ejecución de las instrucciones.

### Tabla de símbolos

Para el manejo de los tipos (en este caso solo NUMERO) y las variables que define el usuario se hace uso de una tabla de símbolos con la que cada clase `Instruccion` hace uso de la misma para ir reemplazando los símbolos por los valores correspondiente o actualizando dichos valores si corresponde según la instruccion a interpretar.

### Main (main.py)

Este archivo contiene el programa principal que integra el lexer y el parser. Se encarga de recibir el código fuente de PYLogo, pasar el texto a través del lexer para realizar el análisis léxico, y luego utilizar el parser para verificar la estructura y ejecutar las instrucciones correspondientes. Además, incluye la inicialización de la interfaz gráfica donde la tortuga ejecuta los comandos y se visualizan los gráficos generados.

### Acciones Semánticas

Las acciones semánticas se ejecutan durante el proceso de análisis, permitiendo que los comandos tengan un efecto en la "tortuga" y en el entorno gráfico.

## Casos de Prueba

Se han creado casos de prueba en la carpeta `test/` para validar el correcto funcionamiento del scanner, parser y las acciones semánticas. Esto incluye pruebas varias y pruebas de los distintos mensajes de error.

## Conclusiones

Este trabajo práctico ha permitido comprender mejor los conceptos de diseño e implementación de un lenguaje de programación básico, así como la importancia de un análisis léxico y sintáctico eficaz para la generacion de código.

## Versión PYLogo

La versión PYLogo consiste en un conjunto limitado de comandos que incluyen acciones básicas como avanzar (`foward`), girar (`left`, `right`) y controlar el estado del lápiz (`penup`, `pendown`). Esto permite a los usuarios crear gráficos básicos sin necesidad de comandos avanzados.

Ejemplo:

```
penup
setpos [100, 100]
foward 100
left 90
foward 50
pendown
foward 50
```

## Acciones disponibles

- Mover tortuga:
  - [x] `forward <exp>`
  - [x] `back <exp>`
  
- Rotar tortuga:
  - [x] `left <exp>`
  - [x] `right <exp>`
  
- Posicionar tortuga:
  - [x] `setpos [<exp> <exp>]`
    
- Centrar tortuga:
  - [x] `home`
    
- Limpiar pantalla:
  - [x] `clean`
  
- Limpiar pantalla y centrar tortuga:
  - [x] `clearscreen`
  
- Mostrar:
  - [x] `show <exp>`
  
- Subir/Bajar lápiz:
  - [x] `pendown`
  - [x] `penup`
  
- Ciclos:
  - [x] `repeat <expr> [ comandos... ]`
  - [x] `while <expr> [ comandos... ]`
  
- Bifurcaciones:
  - [x] `if <expr> [ comandos... ]`
  - [x] `if <expr> [ comandos... ] else [ comandos... ]`
    
- Asignación:
  - [x] `name = NUMERO`
    
- Bloques comandos:
  - [x] `[ comandos...]`

## Ejemplo de programa

```

clearscreen 
penup 
forward 50 
pendown 
repeat 4 [ forward 100 right 90 ] 
home 

clearscreen 
penup 
back 100 
pendown 
repeat 4 [ forward 100 right 90 ] 
home 
```