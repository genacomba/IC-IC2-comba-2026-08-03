### 🟢 D4 — Parámetro por default
#Escribí `aprobo(notas, minimo=6)` donde el umbral de aprobación tiene un valor por default pero se puede cambiar. Probala sin pasar `minimo` y pasando `minimo=7`.
#**Listo cuando:** funciona de las dos formas sin duplicar código.
def promedio(notas):
    total= 0 
    for nota in notas:
        total = total + nota

    return total / len(notas)

def aprobo(notas, minimo=6):
    return promedio(notas) >= minimo

notas_genaro = [4,8,7,6,2,10]
print(aprobo(notas_genaro))
print(aprobo(notas_genaro, 7))