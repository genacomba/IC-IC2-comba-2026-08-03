import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent / "PARTE_B2"))

from main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_listar_libros():
    respuesta = client.get("/libros")

    assert respuesta.status_code == 200


def test_crear_libro_valido():
    libro_valido = {
        "titulo": "El Hobbit",
        "paginas": 322,
        "editorial": {
            "nombre": "Minotauro",
            "pais": "España"
        }
    }

    respuesta = client.post(
        "/libros",
        json=libro_valido
    )

    assert respuesta.status_code in [200, 201]


def test_crear_libro_sin_paginas():
    libro_invalido = {
        "titulo": "Libro inválido",
        "editorial": {
            "nombre": "Editorial Test",
            "pais": "Argentina"
        }
    }

    respuesta = client.post(
        "/libros",
        json=libro_invalido
    )

    assert respuesta.status_code == 422


def test_crear_libro_y_verificarlo():
    libro_nuevo = {
        "titulo": "El Hobbit - E4",
        "paginas": 322,
        "editorial": {
            "nombre": "Minotauro",
            "pais": "España"
        }
    }

    respuesta_post = client.post(
        "/libros",
        json=libro_nuevo
    )

    assert respuesta_post.status_code in [200, 201]

    respuesta_get = client.get("/libros")

    assert respuesta_get.status_code == 200

    libros = respuesta_get.json()

    assert any(
        libro["titulo"] == "El Hobbit - E4"
        for libro in libros
    )