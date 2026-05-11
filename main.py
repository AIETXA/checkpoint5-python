# ===========================
# Ejercicio 1 — Bucle for
# ===========================

jugadores = ['Messi', 'Maradona', 'Aymar', 'Batistuta', 'Romero']

for jugador in jugadores:
    print(jugador)


# ===========================
# Ejercicio 2 — Función suma
# ===========================    

def suma(a,b,c):
    return a + b + c
print(suma(5,10,8))


# ===========================
# Ejercicio 3 — Función suma Lambda
# ===========================    

suma = lambda a,b,c: a + b + c
print(suma(6,7,8))


# ===========================
# Ejercicio 4 — ¿Coincide el valor de la variable?
# ===========================    

nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

if nombre in lista_nombre:
    print(f'{nombre} se encuentra en la lista')
else:
    print(f'{nombre} no se encuentra en la lista')