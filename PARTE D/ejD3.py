### 🔴 D3 — Estadísticas
#Escribí `estadisticas(notas)` que devuelva un **diccionario** con `promedio`, `maximo` y `minimo`.
#**Listo cuando:** una sola llamada te da las tres cosas en un dict.

def promedio(notas):
    total= 0 
    for nota in notas:
        total = total + nota

    return total / len(notas)


def estadisticas (notas):
    return {
        "promedio": promedio(notas),
        "maximo": max(notas),
        "minimo": min(notas)
    }
notas_genaro = [4,8,7,6,2,10]
notas_juan = [5,6,3,2]
print(estadisticas(notas_genaro))
print(estadisticas(notas_juan))