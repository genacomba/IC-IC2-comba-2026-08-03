### 🟢 D1 — Encapsular
#Convertí el cálculo de promedio (A1) en una **función** `promedio(notas)` que reciba una lista y devuelva el número. Probala con dos listas distintas.
#**Listo cuando:** la misma función sirve para cualquier lista.


def promedio(notas):
    total= 0 
    for nota in notas:
        total = total + nota

    return total / len(notas)

notas_genaro = [4,8,7,6,2,10]
notas_juan = [5,6,3,2]
print(promedio(notas_genaro))
print(promedio(notas_juan))