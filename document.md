#🐍 Documentación Python para CheckPoint 5

> **Autor:** Ailén
> **Nivel:** Iniciación
> **Formato:** Markdown
> **Fecha:** Mayo 2026

---

## 📄Tabla de contenidos:

1. [Condicionales](#1-condicionales-en-python)
2. [Diferentes tipos de bucles](#2-tipos-de-bucles-en-python)
3. [Lista por compresión](#3-lista-por-compresión-en-python)
4. [Argumentos](#4-argumentos-en-python)
5. [Función Lambda](#5-funcion-Lambda-en-python)
6. [Paquete pip](#6-paquete-pip-en-python)
7. [Ejercicios prácticos](#7-ejercicios-prácticos-en-python)


## 1. ¿Qué es un condicional? 

Un **condicional** en Python es una estructura de control que permite al programa tomar ciertas decisiones. Evalua si una condicion es verdadera **True** o falsa **False** y ejecuta bloques de codigo segun el resultado.

>💡 **Semejanza:** Como cuando decidís que ponerte basandote en el clima; si hace frío te pondrás un abrigo sino no.

### La estructura básica: el **if**
Es la forma mas simple. Si la condición se cumple (True), el código se ejecuta, sino Python la salta.

```python
clima = 'sol'

if clima == 'sol':
    print('Hace un hermoso día soleado, no olvides tus gafas 🕶️')

```
> 💡 **Tip:** Todo lo que esté "adentro" de un `if` tiene que estar corrido 
> hacia la derecha. Es la forma que tiene Python de entender qué código 
> ejecutar y cuál no.


### Y si no se cumple? el **else**
Sirve para dar una alternativa cuando la primera condición es falsa(False).

```python
clima = 'nublado'

if clima == 'sol':
    print('Hace un hermoso día soleado, no olvides tus gafas 🕶️')
else:
    print('Mejor lleva un paraguas porque parece que va a llover ☔')

```

### Multiples opciones: el **elif**
Lo usamos si tenemos mas de dos posibilidades. Podemos poner tantos como necesitemos.

```python
clima = 'frio'
    
if clima == 'sol':
    print('Hace un hermoso día soleado, no olvides tus gafas 🕶️')
elif clima == 'nublado':
    print('Mejor lleva un paraguas porque parece que va a llover ☔')
elif clima == 'ventoso':
    print('Mejor lleva un rompevientos 🧥🌬️')  
else:
    print('Abrigate bien 🧣🧥')      

```

### Para comparar cosas adentro de un **if** usamos **Operadores de condición**

| Operador | Significado | Ejemplo |
|---|---|---|
| `==` | Igual a | `5 == 5` → `True` |
| `!=` | Diferente de | `5 != 3` → `True` |
| `>` | Mayor que | `7 > 3` → `True` |
| `<` | Menor que | `2 < 8` → `True` |
| `>=` | Mayor o igual | `5 >= 5` → `True` |
| `<=` | Menor o igual | `4 <= 6` → `True` |

### Dicisiones complejas: Operadores lógicos

A menudo tenemos que tomar decisiones basadas en múltiples condiciones. Por ejemplo, podemos querer ejecutar una determinada acción sólo si se cumplen varias condiciones simultáneamente. Alternativamente, podríamos querer desencadenar una acción alternativa si se cumple alguna de varias condiciones.

Python ofrece un conjunto de operadores lógicos **and, or, not** para manejar estos escenarios.

> AND — ambas condiciones deben ser True
```python
buen_tiempo = True
tengo_tiempo = True

if buen_tiempo and tengo_tiempo:
    print('¡Genial! Vamos al parque 🌳')
else:
    print('Me quedo en casa 🏠')
```

> OR — al menos una condición debe ser True
```python
es_domingo = True
es_feriado = False

if es_domingo or es_feriado:
    print('Hoy duermo hasta tarde💤')
```

> NOT — invierte el valor booleano
```python
llueve = False

if not llueve:
    print('Podemos salir a pasear🚶‍➡️')
```

**💡 Tip: El operador not es como el "mundo al revés". Si algo es falso, el not lo vuelve verdadero para que el if pueda entrar a ejecutar el código.**


## 2. ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

Un **bucle** es una estructura que permite ejecutar un bloque de código varias veces de manera automática.

¿Por qué son útiles?
- **Ahorran tiempo:** No tienes que escribir la misma línea de código una y otra vez.
- **Evitan errores:** Menos código escrito a mano significa menos probabilidad de equivocarse.
- **Procesan grandes datos:** Son esenciales para recorrer listas de miles de nombres, precios o mensajes.

> 💡 **Sin bucles**, para imprimir los números del 1 al 100 tendrías que escribir 100 líneas. **Con bucles**, solo necesitas 2.

### Tipos de Bucles:

* 1. El bucle **for** (iteración definida):
Se utiliza para repetir una acción varias veces, recorriendo elementos de una colección(lista, tupla, cadena, rango, etc.). Se sabe de antemano cuántas veces debe ejecutarse el código.

**Sintaxis:** ```for variable in secuencia```
**Uso con range():** Para repetir un código un número específico de veces.

```python
# Imprimir números del 0 al 4
for i in range(5):
    print(i)
```    

* 2. El bucle **while** (iteración indefinida):
Ejecuta un bloque de código continuamente mientras una condición booleana sea True. Se usa cuando no sabes exactamente cuando terminará la repetición.

**Sintáxis:** ```while condición```
**Importante:** Se debe actualizar la condición dentro del bucle para evitar un bucle infinito.
```python
# Imprimir números mientras i sea menor a 5
i = 0
while i < 5:
    print(i)
    i += 1

```

#### Mecanismos de control de bucles:
- **break:** rompe y sale del bucle inmediatamente.
- **continue:** salta la iteración actual y pasa a la siguiente.
- **else:** se ejecuta cuando el bucle finaliza normalmente.

Ejemplo: 
```python
for i in range(10):
    if i == 5:
        break  # Se detiene en el 5
    if i % 2 == 0:
        continue  # Se salta los números pares
    print(i)
```



## 3. ¿Qué es una lista por comprensión en Python?

Es una forma elegante, compacta y rápida de crear una nueva lista basándose en otra secuencia, en solamente una línea de código.
> 💡 Lo que antes tomaba 5 líneas, con comprensión se escribe en 1.

**Sintaxis:** 
```python 
nueva_lista = [expresion    for elemento in secuencia]
                ¿qué hago?          ¿de dónde?  
```

**Forma larga:**
```python
numeros = [1,2,3,4]
duplicados = []

for n in numeros:
    duplicados.append(n*2)
```

**Forma corta:**
```python
duplicados = [n*2 for n in numeros]
```

Traducido en palabras:
`[n*2         for n        in numeros]`
>*"el doble  de cada n  que esta en numeros"*

También podemos agregar **condicionales** que actúan como filtros. Por ejemplo si solo queremos duplicar los números pares que hay en la lista. 

```python
duplicados_pares = [n*2 for n in numeros if n%2 == 0]
```
En palabras: 
`[n*2 for n in numeros if n%2 == 0]`
>*"el doble de cada n que está en numeros pero solo si n es par"*


## 4. ¿Qué es un argumento en Python?

Es el valor real que se envía a una función cuando se la invoca o llama. Los argumentos permiten pasar datos hacia el interior de la función para que ésta realice operaciones con ellos.
Hay que diferenciar los **argumentos** de los **parámetros**, porque es común que nos confundamos.

> 🧑‍🍳 Imaginá que la función es una receta de cocina:
> - **Parámetro** → el nombre del ingrediente en la receta: *"ingrediente"*
> - **Argumento** → el valor real que usás al cocinar: *"maicena"*

```python
def receta(nombre):  # 'nombre' es el PARÁMETRO
    print(f'Hoy vamos a hacer {nombre}') 

receta('Alfajores de maicena')  # 'Alfajores de maicena' es el ARGUMENTO

```
### Tipos de argumentos:

1. **Argumentos posicionales:**
Son los más comunes. Se asignan a los parámetros en el mismo orden en el que se envían.
```python
def describir_persona(nombre, edad):
    print(f"{nombre} tiene {edad} años.")

describir_persona("Ana", 25)  # Correcto: Ana tiene 25 años.
describir_persona(25, "Ana")  # Incorrecto: 25 tiene Ana años.
```

2. **Argumentos de Palabra clave(keywords):**
Permiten enviar los valores indicando explícitamente el nombre del parámetro seguido del signo = . Al usarlos, el orden de los factores no altera el resultado.
```python
describir_persona(edad=25, nombre="Ana")  # Funciona perfectamente igual
```

3. **Argumentos por defecto:**
Podes asignar un valor predeterminado a un parámetro al definir la función. Si al llamarla no proporcionas ese argumento, Python utilizará el valor por defecto.
```python
def saludar_pais(nombre, pais="España"):
    print(f"Hola {nombre} de {pais}")

saludar_pais("Luis")             # Usa el defecto: Hola Luis de España
saludar_pais("Luis", "México")   # Sobrescribe el defecto: Hola Luis de México
``` 

4. **Argumentos variables(*args, **kwargs)**
Se utilizan cuando no sabes de antemano cuántos argumentos va a recibir la función.
- `*args` -> es una forma de decirle a una función "acepta todos los argumentos que te manden sin importar cuantos sean". Los recibe como una **tupla**

- `**kwargs` -> es lo mismo pero pasa argumentos nombrados y los recibe como un **diccionario.**

```python
def sumar(*args):
    print(args)  # (1, 2, 3) ← tupla

def presentar(**kwargs):
    print(kwargs)  # {'nombre': 'Ana', 'edad': 25} ← diccionario

sumar(1, 2, 3)
presentar(nombre="Ana", edad=25)
```
## 5. ¿Qué es una función Lambda en Python?


## 6. ¿Qué es un paquete pip?

