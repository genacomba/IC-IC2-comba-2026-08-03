### 🔴 D6 — Reporte combinado
#Escribí `reporte(notas)` que use `estadisticas()` por dentro y devuelva un **texto** ya armado, tipo: `"Promedio: 7.2 | Máximo: 10 | Mínimo: 4"`.
#**Listo cuando:** una sola llamada te da el texto final, combinando lo que ya hicieron D1-D3.

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

def reporte (notas):
    datos = estadisticas(notas)
    return f"El promedio es {datos["promedio"]:.1f}, el maximo es {datos["maximo"]} y el minimo es {datos["minimo"]}"

notas_genaro = [4,8,7,6,2,10]

print(reporte(notas_genaro))