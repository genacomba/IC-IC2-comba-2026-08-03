### 🔴 C5 — Búsqueda
#Sobre la lista de C4, escribí código que imprima las películas de un director dado. Si en C4 guardaste el nombre completo (ej. `"Christopher Nolan"`), buscar por el nombre completo exacto (`==`) no va a encontrar nada si buscás solo `"Nolan"` — son strings distintos. Elegí una de las dos y probá que ande: (a) comparación exacta con el nombre completo, o (b) `"Nolan" in pelicula["director"]` para que matchee por coincidencia parcial. Si no hay ninguna, que avise.
#**Listo cuando:** encuentra las que matchean con el criterio que elegiste y maneja el caso "ninguna".
peliculas = [
     {
    "titulo": "Relatos salvajes",
    "anio": 2014,
    "director": "Damián Szifron"
    },

    {
        "titulo": "Toy Story",
        "anio": 1995,
        "director": "John Lasseter"
    },
    {
            "titulo": "Cars",
            "anio": 2006,
            "director": "Joe Ranft"
    }
]

director_buscado = "Joe"
encontrada = False
for pelicula in peliculas:
    if director_buscado in pelicula["director"]:
        print("Pelicula encontrada: ", pelicula["titulo"])
        encontrada = True

if encontrada == False:
    print("Ninguna encontrada")