### 🟡 E1 — Leer y mostrar
#Abrí el CSV y mostrá cada línea por pantalla.
#**Listo cuando:** ves el contenido del archivo desde Python.
archivo = open("IC-IC2-comba-2026-08-03/PARTE E/peliculas.csv", "r")
for linea in archivo:
    print(linea)
archivo.close()