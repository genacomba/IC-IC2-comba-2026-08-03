### 🟡 B3 — El más alto y el más bajo
#Dada la lista de puntajes `[120, 45, 300, 80, 210]`, imprimí el mayor, el menor y el promedio. **No uses** `max()`/`min()` la primera vez: hacelo con un `for`. Después comparalo con `max()`/`min()`.
#**Listo cuando:** tu versión con `for` da lo mismo que la de las funciones.

puntajes = [120, 45, 300, 80, 210]
menor = puntajes[0]
mayor = puntajes[0]
total = 0

for puntaje in puntajes:
    total = puntaje + total
    if puntaje > mayor:
        mayor = puntaje
    if puntaje < menor:
        menor = puntaje

promedio = total / len(puntajes)

print(mayor)
print(menor)
print(promedio)

print(max(puntajes))
print(min(puntajes))