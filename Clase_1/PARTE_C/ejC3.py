### 🟡 C3 — Clave que no existe
#Intentá acceder a `pelicula["duracion"]` (que no existe) y mirá el error. Después conseguí que, si la clave no está, devuelva `"desconocido"` en vez de romper. Investigá `.get()`.
#**Listo cuando:** no se rompe aunque la clave falte.

pelicula = {
    "titulo": "Relatos salvajes",
    "anio": 2014,
    "director": "Damián Szifron"
}

print(pelicula.get("duracion", "desconocido"))
