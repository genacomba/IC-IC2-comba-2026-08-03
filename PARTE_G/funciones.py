def promedio(notas):
    if not notas:
        return "No hay notas"
    total= 0 
    for nota in notas:
        total = total + nota

    return total / len(notas)

notas_genaro = [4,8,7,6,2,10]
notas_juan = [5,6,3,2]

def aprobo(notas):
    return promedio(notas) >= 6

def estadisticas (notas):
    return {
        "promedio": promedio(notas),
        "maximo": max(notas),
        "minimo": min(notas)
    }

def obtener_dato(pelicula, clave):
    return pelicula.get(clave, "desconocido")
