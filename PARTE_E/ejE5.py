### 🔴 E5 — Agrupar por categoría
#Usando el CSV con `genero` de E4, calculá el **puntaje promedio por género** (un diccionario `{genero: promedio}`).
#**Listo cuando:** cada género del archivo aparece una vez en el resultado, con su promedio correcto.

archivo = open("IC-IC2-comba-2026-08-03/PARTE E/peliculas.csv", "r")
sumas = {}
cantidades = {}

next(archivo)
for linea in archivo:
    linea = linea.strip()
    datos = linea.split(",")

    puntaje = float(datos[2])
    genero = datos[3]

    if genero in sumas:
        sumas[genero] = sumas[genero] + puntaje
        cantidades[genero] = cantidades [genero] + 1
    else:
        sumas[genero] = puntaje
        cantidades[genero] = 1

promedios = {}
for genero in sumas:
    promedios[genero] = sumas[genero] / cantidades [genero]

archivo.close()
print(promedios)

