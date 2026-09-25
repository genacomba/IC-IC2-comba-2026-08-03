#🟡 A4 — JSON a mano
#Escribí en JSON (texto) un libro con titulo, autor, paginas y disponible (verdadero/falso). Después escribí una lista de 2 libros. Por último, escribí un libro que tenga un campo anidado: editorial con nombre y pais. Listo cuando: el JSON es válido (probalo en cualquier validador), notás que se parece a un dict/lista de Python, y entendés que un dict anidado en Python es lo mismo que un objeto anidado en JSON.
import json


libro = {
    "titulo": "El Principito",
    "autor": "Antoine de Saint-Exupéry",
    "paginas": 96,
    "disponible": True
}



libros = [
    {
        "titulo": "El Principito",
        "autor": "Antoine de Saint-Exupéry",
        "paginas": 96,
        "disponible": True
    },
    {
        "titulo": "1984",
        "autor": "George Orwell",
        "paginas": 328,
        "disponible": False
    }
]

libro_con_editorial = {
    "titulo": "El Principito",
    "autor": "Antoine de Saint-Exupery",
    "paginas": 96,
    "disponible": True,
    "editorial": {
        "nombre": "Salamandra",
        "pais": "Espana"
    }
}

print(json.dumps(libro_con_editorial, indent=2))