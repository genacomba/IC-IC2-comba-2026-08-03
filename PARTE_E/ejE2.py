### 🟡 E2 — Cuidado: todo viene como texto
#Sumá la columna `puntaje` de todas las películas. Vas a chocar con que los números vienen como **texto**. Resolvelo.
#**Listo cuando:** la suma da un número y entendés por qué había que convertir.
archivo = open("IC-IC2-comba-2026-08-03/PARTE E/peliculas.csv", "r")
suma=0
next(archivo)
for linea in archivo:
    datos = linea.split(",")
    suma = float(datos[2]) + suma
archivo.close()
print(suma)