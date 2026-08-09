### 🟡 E4 — Filtrar y guardar
#Agregale una columna `genero` **al mismo** `peliculas.csv` que ya venís usando desde E1 (no crees un archivo nuevo con otro nombre — si lo hacés, terminás con dos versiones del dataset y los resultados de E1-E3 y E4-E5 dejan de coincidir). Editalo a mano. Leé el archivo, quedate solo con las películas de un género elegido, y escribí un **nuevo CSV** (`filtradas.csv`) solo con esas.
#**Listo cuando:** el nuevo CSV existe, tiene menos filas que el original (que ahora incluye la columna `genero`), y lo pueden abrir y verificar a ojo.

archivo = open("IC-IC2-comba-2026-08-03/PARTE E/peliculas.csv", "r")
nuevo = open("IC-IC2-comba-2026-08-03/PARTE E/filtradas.csv", "w")
genero = "animacion"
nuevo.write("titulo,anio,puntaje,genero\n")
next(archivo)
for linea in archivo:
    linea = linea.strip()
    datos = linea.split(",")
    if datos[3] == genero:
        nuevo.write(linea +"\n" )
archivo.close
nuevo.close
