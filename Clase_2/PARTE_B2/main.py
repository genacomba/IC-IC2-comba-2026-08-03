from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class Editorial(BaseModel):
    nombre: str
    pais: str


class Libro(BaseModel):
    titulo: str
    paginas: int = Field(gt=0)
    editorial: Editorial
    disponible: bool = True


libros = [
    {
        "titulo": "El Principito",
        "paginas": 96,
        "editorial": {
            "nombre": "Salamandra",
            "pais": "España"
        }
    },
    {
        "titulo": "1984",
        "paginas": 328,
        "editorial": {
            "nombre": "Debolsillo",
            "pais": "España"
        }
    },
    {
        "titulo": "Don Quijote de la Mancha",
        "paginas": 863,
        "editorial": {
            "nombre": "Alfaguara",
            "pais": "España"
        }
    }
]


autores = [
    {"nombre": "Antoine de Saint-Exupéry"},
    {"nombre": "George Orwell"},
    {"nombre": "Miguel de Cervantes"}
]


@app.get("/")
def inicio():
    return {"mensaje": "hola"}


@app.get("/libros")
def listar_libros(paginas_min: int | None = None):
    if paginas_min is None:
        return libros

    return [
        libro for libro in libros
        if libro["paginas"] >= paginas_min
    ]


@app.post("/libros")
def crear_libro(libro: Libro):
    libros.append(libro.model_dump())
    return libro


@app.get("/libros/{titulo}")
def buscar_libro(titulo: str):
    for libro in libros:
        if libro["titulo"] == titulo:
            return libro

    raise HTTPException(
        status_code=404,
        detail="Libro no encontrado"
    )


@app.put("/libros/{titulo}")
def actualizar_libro(titulo: str, libro_nuevo: Libro):
    for i, libro in enumerate(libros):
        if libro["titulo"] == titulo:
            libros[i] = libro_nuevo.model_dump()
            return libros[i]

    raise HTTPException(
        status_code=404,
        detail="Libro no encontrado"
    )


@app.delete("/libros/{titulo}", status_code=204)
def eliminar_libro(titulo: str):
    for i, libro in enumerate(libros):
        if libro["titulo"] == titulo:
            libros.pop(i)
            return

    raise HTTPException(
        status_code=404,
        detail="Libro no encontrado"
    )


@app.get("/autores")
def listar_autores():
    return autores


@app.post("/autores")
def crear_autor(autor: dict):
    autores.append(autor)
    return autor