### 🟡 C4 — Lista de diccionarios
#Armá una lista de **3 películas** (cada una un diccionario como C1). Recorrela con un `for` e imprimí solo los títulos.
#**Listo cuando:** imprime los 3 títulos. (Esto es *exactamente* la forma en que la API te va a devolver datos en la clase 2.)
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

for pelicula in peliculas:
    print(pelicula["titulo"])