# Utilizando Python y PLY (Python Lex-Yacc), vamos a descomponer el proceso en varias etapas. El objetivo es que entiendas cómo estructurar el lexer y parser, y cómo implementar las funcionalidades solicitadas en tu lenguaje.


# Parseo Logo UNaHur
```
Mover tortuga:
- foward <exp>
- back <exp>

Rotar tortuga:
- left <exp>
- right <exp>

Posicionar tortuga:
- setpos [<exp> <exp>]
- setx <exp>
- sety <exp>

Obtener posicion tortuga:
- xcor
- ycor
- pos

Centrar tortuga:
- home 

Mostrar/Ocultar tortuga:
- showturtle
- hideturtle

Limpiar pantalla:
- clean

Limpiar pantalla y centrar tortuga:
- clearscreen

Mostrar:
- show <exp>

Subir/Bajar lapiz:
- pendown
- penup

Ciclos:
- repeat <expr> [ comandos... ]
- while <expr> [ comandos...]

Bifurcaciones:
- if <expr> [ comandos... ]
- ifelse <expr> [ comandos... ] [ comandos... ]

Procedimiento:
- to <proc_name> <inputs> <comandos> end

Asignacion_
- name <expr> varname

Referencia:
- :varname

Listas de palabras o listas, separadas por espacion en blanco:
- [ word ... ]

Bloques comandos:
- [ comandos...]
```

### Ejemplo de programa

```

to cuadrado :largo
  repeat 4 [ forward :largo right 90 ]
end



clearscreen
penup
forward 300
pendown
cuadrado 100
home
if xcor < 100 [ hideturtle ]

```
