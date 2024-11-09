# Parseo y Generación de Código

## Trabajo Práctico

**Profesor:** Mag. Ing. Pablo Pandolfo

**Alumnos:**
- Ferrara Facundo Matias
- Origlia Pablo

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
cd proyecto
```

3. Crear y Configurar los Archivos  
Una vez en el directorio, puedes proceder a crear los archivos `lexer.py` y `parser.py` con el código que mencioné antes:

- `lexer.py`: Contiene el análisis léxico.
- `parser.py`: Contiene el análisis sintáctico y el programa principal.

Asegúrate de tener las dependencias necesarias instaladas, como PLY y Tkinter.

4. Instalar Dependencias  
El proyecto utiliza Python y tiene un archivo `requirements.txt`, puedes instalar las dependencias con:

pip install -r requirements.txt

5. Ejecutar el Programa  
Una vez todo esté en su lugar, puedes ejecutar el archivo `parser.py`:

## Definición del Lenguaje

PYLogo es un lenguaje de programación basado en comandos simples que permite a los usuarios interactuar con una "tortuga" para crear gráficos en un plano de coordenadas.

## Implementación

### Scanner

Se ha implementado un scanner que analiza el código fuente de PYLogo, identificando los diferentes tokens que se utilizan en el lenguaje.

Este archivo se encarga del análisis léxico del lenguaje PYLogo. Define los diferentes tokens que componen el lenguaje, como comandos y identificadores, utilizando la biblioteca PLY para crear un lexer que identifica y clasifica los elementos del código fuente. El lexer ignora espacios y saltos de línea, y genera errores para caracteres no válidos.

### Parser

El parser se encarga de analizar la estructura del código PYLogo, validando que los comandos sigan la gramática definida.

El parser es responsable del análisis sintáctico del lenguaje PYLogo. Utiliza la biblioteca PLY para definir la gramática del lenguaje, validando que los comandos en el código fuente cumplan con las reglas sintácticas. El parser organiza las estructuras de los comandos y controla la correcta jerarquía de ejecución de las instrucciones.

### Main (main.py)

Este archivo contiene el programa principal que integra el lexer y el parser. Se encarga de recibir el código fuente de PYLogo, pasar el texto a través del lexer para realizar el análisis léxico, y luego utilizar el parser para verificar la estructura y ejecutar las instrucciones correspondientes. Además, puede incluir la inicialización de la interfaz gráfica donde la tortuga ejecuta los comandos y se visualizan los gráficos generados.

### Acciones Semánticas

Las acciones semánticas se ejecutan durante el proceso de análisis, permitiendo que los comandos tengan un efecto en la "tortuga" y en el entorno gráfico.

## Casos de Prueba Automatizados

Se han creado casos de prueba automatizados para validar el correcto funcionamiento del scanner, parser y las acciones semánticas. Esto incluye pruebas unitarias y pruebas de integración.

## Conclusiones

Este trabajo práctico ha permitido comprender mejor los conceptos de diseño e implementación de un lenguaje de programación, así como la importancia de un análisis léxico y sintáctico eficaz.

## Versión PYLogo

La versión PYLogo consiste en un conjunto limitado de comandos que incluyen acciones básicas como avanzar (AVANZA), girar (GIRA_IZQUIERDA, GIRA_DERECHA) y controlar el estado del lápiz (LEVANTA_PLUMA, BAJA_PLUMA). Esto permite a los usuarios crear gráficos básicos sin necesidad de comandos avanzados.

Ejemplo:

Tortuga(600, 600); START AVANZA(100); GIRA_IZQUIERDA(90); AVANZA(50); BAJA_PLUMA(); AVANZA(50); END

## Acciones disponibles

- Mover tortuga:
  - [x] `forward <exp>`
  - [ ] `back <exp>`
  
- Rotar tortuga:
  - [x] `left <exp>`
  - [ ] `right <exp>`
  
- Posicionar tortuga:
  - [ ] `setpos [<exp> <exp>]`
  - [ ] `setx <exp>`
  - [ ] `sety <exp>`
  
- Obtener posición tortuga:
  - [ ] `xcor`
  - [ ] `ycor`
  - [ ] `pos`
  
- Centrar tortuga:
  - [ ] `home`
  
- Mostrar/Ocultar tortuga:
  - [ ] `showturtle`
  - [ ] `hideturtle`
  
- Limpiar pantalla:
  - [ ] `clean`
  
- Limpiar pantalla y centrar tortuga:
  - [ ] `clearscreen`
  
- Mostrar:
  - [ ] `show <exp>`
  
- Subir/Bajar lápiz:
  - [ ] `pendown`
  - [ ] `penup`
  
- Ciclos:
  - [x] `repeat <expr> [ comandos... ]`
  - [x] `while <expr> [ comandos... ]`
  
- Bifurcaciones:
  - [x] `if <expr> [ comandos... ]`
  - [x] `ifelse <expr> [ comandos... ] [ comandos... ]`
  
- Procedimiento:
  - [ ] `to <proc_name> <inputs> <comandos> end`
  
- Asignación:
  - [ ] `name <expr> varname`
  
- Referencia:
  - [ ] `:varname`
  
- Listas de palabras o listas, separadas por espacio en blanco:
  - [ ] `[ word ... ]`
  
- Bloques comandos:
  - [ ] `[ comandos...]`

## Ejemplo de programa

to cuadrado
repeat 4 [ forwardright 90 ] end

clearscreen penup forward 300 pendown cuadrado 100 home if xcor < 100 [ hideturtle ] go

clearscreen penup forward 300 pendown cuadrado 100 home if xcor < 100 [ hideturtle ] go
