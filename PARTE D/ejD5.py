### 🟡 D5 — Que no explote con la lista vacía
#Llamá a `promedio([])`. Va a fallar (`ZeroDivisionError`). Decidí qué debería pasar en ese caso (¿devolver `0`? ¿avisar con un mensaje?) y programalo.
#**Listo cuando:** `promedio([])` ya no revienta el programa, y elegiste a propósito qué hace en su lugar.

def promedio(notas):
    if not notas:
        return "No hay notas"
    total= 0 
    for nota in notas:
        total = total + nota

    return total / len(notas)

print(promedio([]))