from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

import os
import psycopg

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

def obtener_conexion():
    return psycopg.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        dbname=os.environ["DB_NAME"],
    )
@app.get("/")
def inicio():
    return {"mensaje": "hola"}


@app.get("/libros")
def listar_libros(paginas_min: int | None = None):
    conexion = obtener_conexion()

    try:
        with conexion.cursor() as cursor:
            if paginas_min is None:
                cursor.execute("""
                    SELECT id, titulo, paginas,
                           editorial_nombre, editorial_pais, disponible
                    FROM libros
                """)
            else:
                cursor.execute("""
                    SELECT id, titulo, paginas,
                           editorial_nombre, editorial_pais, disponible
                    FROM libros
                    WHERE paginas >= %s
                """, (paginas_min,))

            filas = cursor.fetchall()

        libros_resultado = []

        for fila in filas:
            libros_resultado.append({
                "id": fila[0],
                "titulo": fila[1],
                "paginas": fila[2],
                "editorial": {
                    "nombre": fila[3],
                    "pais": fila[4]
                },
                "disponible": fila[5]
            })

        return libros_resultado

    finally:
        conexion.close()


@app.post("/libros")
def crear_libro(libro: Libro):
    conexion = obtener_conexion()

    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                INSERT INTO libros (
                    titulo,
                    paginas,
                    editorial_nombre,
                    editorial_pais,
                    disponible
                )
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id
            """, (
                libro.titulo,
                libro.paginas,
                libro.editorial.nombre,
                libro.editorial.pais,
                libro.disponible
            ))

            id_libro = cursor.fetchone()[0]

        conexion.commit()

        return {
            "id": id_libro,
            **libro.model_dump()
        }

    finally:
        conexion.close()


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

@app.get("/salud")
def salud():
    host = os.environ["DB_HOST"]
    user = os.environ["DB_USER"]
    password = os.environ["DB_PASSWORD"]
    dbname = os.environ["DB_NAME"]

    try:
        with psycopg.connect(
            host=host,
            user=user,
            password=password,
            dbname=dbname,
        ):
            return {
                "estado": "ok",
                "mensaje": "Conexión a PostgreSQL exitosa"
            }

    except Exception as e:
        return {
            "estado": "error",
            "mensaje": "No se pudo conectar a PostgreSQL",
            "motivo": str(e)
        }