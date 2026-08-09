### 🔴 E3 — Reporte
#Imprimí: cuántas películas hay, el puntaje promedio, y el título de la mejor puntuada.
#**Listo cuando:** los tres datos salen correctos del archivo real.
archivo = open("IC-IC2-comba-2026-08-03/PARTE E/peliculas.csv", "r")
cantidad=0
suma= 0 
puntaje_max = 0
titulo = ""
next(archivo)

for linea in archivo:
    datos = linea.split (",")
    puntaje = float(datos[2])
    cantidad = cantidad + 1
    suma = suma + puntaje
    if puntaje > puntaje_max:
        puntaje_max = puntaje
        titulo= datos[0]

promedio = suma / cantidad

archivo.close()
print(cantidad)
print(promedio)
print(titulo)




